import unittest

from src.game.MainBoard import MainBoard


class MainBoardTests(unittest.TestCase):

    def test_player_cannot_play_on_board_that_isnt_next(self):
        # Given...
        # ...we instantiate the MainBoard to play on
        main_board = MainBoard()
