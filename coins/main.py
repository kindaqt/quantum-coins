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
steps = []
step = flip | touch | land
steps = [
    { 
        type: "flip"
    },
    {
        type: "touch",
        options: [ 0, 1 ] # coins you want to touch
    },
    {
        type: "land"
    }
]

request.data = {
    coins: [ "heads", "tails" ], #Array<str:["heads","tails"]>
    steps: [{ 
        type: "flip",
        options: {
            coins: [ 0, 1 ] #Array of ints such that each element maps to a coin in the coins array
        }
    }, { 
        type: "touch",
        options: {
            coins: [ 0, 1 ] #Array of ints such that each element maps to a coin in the coins array
        }
    }, {
        type: "land",
        options: {
            coins: [ 0, 1 ] #Array of ints such that each element maps to a coin in the coins array
        }
    }]
}
"""


class Game:
    def __init__(self, coins, steps, simulator='statevector'):
        logging.info(f"initializing coins {coins}")

        self._coins = coins
        self._steps = steps
        self._simulator = AerSimulator(method=simulator)

    def setup(self):
        self._setup_circuit()
        self._setup_states()
        self._setup_steps()

    def _setup_circuit(self):
        n_coins = len(self._coins)
        self._qc = QuantumCircuit(n_coins, n_coins)

    def _setup_states(self):
        coins = self._coins
        qc = self._qc

        # Initialize circuit based on coin states
        for i in range(len(coins)):
            type = coins[i]
            logging.info(f"finding initial state of coin={i} type={type}")
            if type == 'heads':
                state = [0, 1]  # label: 1
            elif type == 'tails':
                type = [1, 0]  # label: 0
            # TODO: unknown state in superposition
            else:
                raise Exception(f"invalid state coin={i} type={type}")

            logging.info(f"initial state coin={i} type={type}")
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
                self.flip(step["options"]["coins"])
            elif step_type == 'touch':
                coins = step["options"]["coins"]
                self.touch(coins[0], coins[1])
            elif step_type == 'land':
                self.land(step["options"]["coins"])
            else:
                raise Exception(f"invalid step of {step}")

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

    def result(self):
        result = self._result
        statevector = result.get_statevector()
        statevector_plot_state_city = plot_state_city(statevector, title='Bell State')
        counts = result.get_counts()
        counts_plot_histogram = plot_histogram(counts, title='Bell State Counts')

        return result, statevector, statevector_plot_state_city, counts, counts_plot_histogram
