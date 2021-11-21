import logging

from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.quantumregister import Qubit
from qiskit.providers.aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.tools.visualization import plot_histogram, plot_state_city, plot_bloch_vector

import numpy as np


class HilbertSpace:
    def __init__(self, coins):
        circuit = QuantumCircuit(1, 1)

        


class Coin:

    _initial_states = {
        "heads": "0",  # 0 state
        "tails": "1",  # 1 state
    }
    _register = None

    def __init__(self, name=None, initial_state="heads", quantum_register=None, quantum_curcuit=None):
        """Create a new coin.

        Args:
            name (string, optional): [description]. Defaults to None.
            initial_state (string or list(int), optional): "heads", "tails", "0", "1", "+", "-", "r", "l", or a ket. Defaults to "heads".
            quantum_register (QuantumRegister, optional): [description]. Defaults to None.
            quantum_curcuit (QuantumCircuit, optional): [description]. Defaults to None.
        """
        print(f'msg="new circuit" name="{name}", initial_state="{initial_state}"')

        qc = quantum_curcuit or QuantumCircuit()
        qr = quantum_register or QuantumRegister(name, bits=[Qubit()])
        qc.add_register(qr)

        initial_state_label = self._initial_states.get(initial_state) or initial_state
        state = Statevector.from_label(initial_state_label)
        qc.initialize(state, 0)
        qc.measure_all()
        qc.save_statevector()

        self.qc = qc


    def flip(self):
        self.qc.h(0)

    def land(self):
        self.qc.h(0)


    def view(self):
        print(self.qc.draw())

        sim = AerSimulator(method="statevector")
        simulation = sim.run(self.qc, validate=True)
        result = simulation.result()

        counts = result.get_counts()
        print(f"counts={counts}")
        statevector = result.get_statevector()
        print(f"statevector={statevector}")

        counts_plot_histogram = plot_histogram(counts, title='Bell State Counts')
        print(f"counts_plot_histogram={counts_plot_histogram}")
        statevector_plot_state_city = plot_state_city(statevector, title='Bell State')
        print(f"statevector_plot_state_city={statevector_plot_state_city}")

    
if __name__ == '__main__':
    coin = Coin(initial_state="1")
    coin.view()
    coin.flip()
    coin.view()
    coin.land()
    coin.view()
