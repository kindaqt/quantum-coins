from coins.main import Game
import unittest
import coins
import pprint


class TestCoins(unittest.TestCase):

    def test_init(self):
        test_coins = ["heads", "tails"]
        test_steps = [
            {
                "type": "flip",
                "options": {
                    "coins": [0, 1]
                }
            }, 
            {
                "type": "touch",
                "options": {
                    "coins": [0, 1]
                }
            }, 
            {
                "type": "land",
                "options": {
                    "coins": [0, 1]
                }
            }
        ]

        game_1 = Game(test_coins, test_steps)
        game_1.setup()
        game_1.play()
        
        print(game_1.result())

    # def test__init__(self):
    #     test_coins = [
    #         {'initial_state': 'heads'},
    #         {'initial_state': 'tails'}
    #     ]
    #     coins_instance = Coins(test_coins)

    #     print(coins_instance.draw())

    #     coins_instance.flip([0,1])
    #     # coins_instance.touch(0,1)
    #     coins_instance.land([0,1])

    #     print(coins_instance.draw())

    #     coins_instance.run(shots=10, memory=False)
    #     print('!!! result=', coins_instance.result)

    #     print('!!! results=', coins_instance.results.get(statevector=True, counts=True))

    # def test_init_circuit():
    #     return

    # def test_flip():
    #     return

    # def test_touch():
    #     return

    # def test_land():
    #     return

    # def test_run():
    #     return

    # def test_reset():
    #     return

    # def test_draw():
    #     return

    # def test_scenarios():
    #     test_initial_states = ["heads", "tails", "invalid"]
    #     test_steps = ["flip", "touch", "land"]


if __name__ == '__main__':
    unittest.main()
