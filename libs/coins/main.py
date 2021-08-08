import logging
from pprint import pprint

from qiskit import QuantumCircuit, compiler
from qiskit.providers.aer import Aer, AerSimulator

import qiskit.quantum_info as qi
from qiskit.tools.visualization import plot_histogram, plot_state_city


# coin = {
#     initial_state: 'heads' or 'tails' // heads is [0,1] and tails is [1,0]
# }

"""
request.data = {
    "coins": [ "heads", "tails", "sides" ]>
    "steps": [{ 
        "type": "flip",
        "coins": [ 0, 1, 2 ] #Array of ints such that each element maps to a coin in the coins array
    }, { 
        "type": "touch",
        "coins": [ 0, 1 ] #Array of ints such that each element maps to a coin in the coins array
    }, {
        "type": "land",
        "coins": [ 0, 1, 2 ] #Array of ints such that each element maps to a coin in the coins array
    }]
}
"""


class Game:
    def __init__(self, coins=None, steps=None, simulator='statevector'):
        print(
            "+---------------------------------------------------------------------+\n", 
            "| Hello and welcome to the quantum realm where spooky actions abound! |\n",
            "+---------------------------------------------------------------------+\n", 
        )
        logging.info(f"initializing game coins={coins} steps={steps} simulator={simulator}")
        self._coins = coins or []
        self._steps = steps or []
        self._simulator = AerSimulator(method=simulator)
        logging.info(f"initializing game coins={coins} steps={steps} simulator={simulator}")

    def setup(self):
        self._setup_circuit()
        self._setup_states()
        self._setup_steps()

    def _setup_circuit(self):
        n_coins = len(self.coins)
        self._qc = QuantumCircuit(n_coins, n_coins)

    def _setup_states(self):
        qc = self._qc

        # Initialize circuit based on coin states
        for i in range(len(self.coins)):
            coin_type = self.coins[i]
            logging.info(f"finding initial state of coin={i} type={coin_type}")

            if coin_type == 'heads':
                state = [0, 1]  # label: 1
            elif coin_type == 'tails':
                state = [1, 0]  # label: 0
            elif coin_type == 'sides':
                state = [.5, .5] # label: + or -
            else:
                raise Exception(f"invalid state coin={i} type={coin_type}")

            logging.info(f"initial state coin={i} type={coin_type}")
            qc.initialize(state, i)
        qc.barrier()

        # Assign circuit
        self._qc = qc

    def _setup_steps(self):
        steps = self._steps

        logging.info(f"setting up steps={steps}")

        for step in steps:
            logging.info(f"setting up step={step}")
            step_type = step["type"]
            if step_type == 'flip':
                self.flip(step["coins"])
            elif step_type == 'touch':
                coins = step["coins"]
                self.touch(coins[0], coins[1])
            elif step_type == 'land':
                self.land(step["coins"])
            else:
                raise Exception(f"invalid step of {step}")

    def get_coins(self):
        return self._coins
    def set_coins(self, coins):
        self._coins = coins
    def del_coins(self):
        del self._coins
    coins = property(get_coins, set_coins, del_coins)

    def get_steps(self):
        return self._steps
    def set_steps(self, steps):
        self._steps = steps
    def del_steps(self):
        del self._steps
    steps = property(get_steps, set_steps, del_steps)

    def flip(self, coins):
        for coin in coins:
            self._qc.h(coin)
        self._qc.barrier()

    def touch(self, control, target):
        """
        Simulates two quantum coins touching. When the coins are in superpostition they become entangled. When the coins are not in superposition they do not become entangled.

        Args:
            control (int): control qubit
            target (int): target qubit

        TODO: support entanglement of n qubits rather than just 2.
        """

        self._qc.cx(control, target)
        self._qc.barrier()

    def land(self, coins):
        for coin in coins:
            self._qc.measure(coin, coin)
        self._qc.barrier()

    def play(self):        
        # Tell simulator to save state vectors
        self._qc.save_statevector()
        # Run simulation
        job = self._simulator.run(self._qc, validate=True)
        # Get result
        result = job.result()

        self._result = result
        return self._result

    def get_result(self):
        statevector = self._result.get_statevector()
        statevector_plot_state_city = plot_state_city(statevector, title='Bell State')
        counts = self._result.get_counts()
        counts_plot_histogram = plot_histogram(counts, title='Bell State Counts')

        return self._result, statevector, statevector_plot_state_city, counts, counts_plot_histogram
    result = property(get_result)
