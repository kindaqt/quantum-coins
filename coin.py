from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

print("HELLO")

svsim = Aer.get_backend('statevector_simulator') # Tell Qiskit how to simulate our circuit

# coin = {
#     initial_state: 'heads' or 'tails' // heads is [0,1] and tails is [1,0]
# }

class Coins:
    def __init__(self, coins):
        print(f"initializing coins {coins}")
        n_coins = len(coins)
        qc = QuantumCircuit(n_coins)

        for i in range(len(coins)):
            coin = coins[i]
            print(f"finding initial state of coin {i} {coin}")

            # TODO: unknown state in superposition
            initial_state = coin["initial_state"]
            if initial_state == 'heads':
                initial_state = [0,1]
            elif initial_state == 'tails':
                initial_state = [1,0]
            else:
                raise Exception(f"invalid initial_state of {coin.initial_state}")
            
            print(f"initial state of coin {i} is {initial_state}")
            qc.initialize(initial_state, i)
        
        self.qc = qc

    def flip(self, coin_i):
        self.qc.h(coin_i)
    
    def land(self):
        self.qc.measure_all()

    def touch(self, coin_0, coin_1):
        self.qc.cx(coin_0, coin_1)
        
    def reset(self):
        self.qc.reset()

    def draw(self):
        return self.qc.draw()


