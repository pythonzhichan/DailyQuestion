import unittest
from day_2 import GuessGame


class TestGuessGame(unittest.TestCase):

    def test_is_range_and_times_int(self):
        game = GuessGame(1, 100, 5)
        self.assertIsInstance(game.min_int, int)
        self.assertIsInstance(game.max_int, int)
        self.assertIsInstance(game.times, int)


if __name__ == '__main__':
    unittest.main()
