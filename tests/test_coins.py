from libs.coins.main import Game
import unittest

class TestGame(unittest.TestCase):

    def test_scenario(self):
        game = Game()
        game.coins = ["heads", "tails", "sides"]
        print(game.coins)
        del game.coins[0]
        print(game.coins)
        game.coins[0] = "basdf"
        print(game.coins)
        # game.coins.set(["heads", "tails", "sides"])


        # print("coins =", game.coins.get_all())

    # def test_init(self):
    #     test_coins = ["heads", "tails"]
    #     test_steps = [
    #         {
    #             "type": "flip",
    #             "coins": [0, 1]
    #         },
    #         {
    #             "type": "touch",
    #             "coins": [0, 1]
    #         },
    #         {
    #             "type": "land",
    #             "coins": [0, 1]
    #         }
    #     ]

    #     game_1 = Game(test_coins, test_steps)
    #     game_1.setup()
    #     game_1.play()

    #     print(game_1.result())


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
