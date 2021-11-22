import logging

from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.bit import Bit
from qiskit.circuit.classicalregister import Clbit
from qiskit.circuit.quantumregister import Qubit
from qiskit.providers.aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.quantum_info.states.quantum_state import QuantumState
from qiskit.result.counts import Counts
from qiskit.tools.visualization import plot_histogram, plot_state_city, plot_bloch_vector


class Game():
    coins = []

    def append(self, coin=None):
        self.qc = QuantumCircuit()
        self.coins.append(Coin(self.qc))
        print(self.qc.draw())

    def result(self):
        print(self.qc.draw())

        self.qc.save_statevector()

        sim = AerSimulator(method="statevector")
        simulation = sim.run(self.qc, validate=True)
        result = simulation.result()

        counts = result.get_counts()
        print(f"counts={counts}")

        statevector = result.get_statevector()
        print(f"statevector={statevector}")

        counts_plot_histogram = plot_histogram(
            counts, title='Bell State Counts')
        print(f"counts_plot_histogram={counts_plot_histogram}")

        statevector_plot_state_city = plot_state_city(
            statevector, title='Bell State')
        print(f"statevector_plot_state_city={statevector_plot_state_city}")


class Coin():
    def __init__(self, circuit, state_label="0", state_vector=None):
        self.qc = circuit
        self.qubit = Qubit()
        qr = QuantumRegister(bits=[self.qubit])
        self.clbit = Clbit()
        cr = ClassicalRegister(bits=[self.clbit])
        self.qc.add_register(qr, cr)
        self.qc.initialize(Statevector.from_label(state_label))

        print('New Coin:')
        print(self.qc.draw())

    def __del__(self):
        self.qc.qubits.remove(self.qubit)
        self.qc.clbits.remove(self.clbits)

    def flip(self):
        self.qc.h(self.qubit)

    def view(self):
        self.qc.measure(self.qubit, self.clbit)

    def land(self):
        self.qc.h(self.qubit)

    def touch(self, target):
        self.qc.cx(self.qubit, target)


if __name__ == '__main__':
    game = Game()
    game.append()
    
    game.coins[0].flip()
    game.coins[0].view()
    game.result()
