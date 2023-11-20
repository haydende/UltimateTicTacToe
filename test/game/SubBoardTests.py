import unittest

from src.exception.BoardIsCompleteError import BoardIsCompleteError
from src.exception.InvalidPositionError import InvalidPositionError
from src.game.SubBoard import SubBoard


def fill_positions_without_win(sub_board):
    sub_board.claim_position(0, "X")
    sub_board.claim_position(4, "O")
    sub_board.claim_position(8, "X")
    sub_board.claim_position(6, "O")
    sub_board.claim_position(2, "X")
    sub_board.claim_position(1, "O")
    sub_board.claim_position(3, "X")
    sub_board.claim_position(5, "O")
    sub_board.claim_position(7, "X")


def fill_positions_with_win(sub_board, winning_player, losing_player):
    sub_board.claim_position(0, winning_player)
    sub_board.claim_position(1, losing_player)
    sub_board.claim_position(3, winning_player)
    sub_board.claim_position(2, losing_player)
    sub_board.claim_position(6, winning_player)


class SubBoardTests(unittest.TestCase):

    def test_cannot_add_to_filled_space(self):
        """
        When attempting to add an entry to a filled position of the board,
        an Exception should be thrown to illustrate that this can't happen.
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # ...position 1 is taken by X
        sub_board.claim_position(1, "X")

        # ...I establish that I expect an InvalidPositionError to be raised
        with self.assertRaises(InvalidPositionError) as cm:
            # When...
            # ...I try to claim position 1 again as "O"
            sub_board.claim_position(1, "X")

        # Then...
        # ...I capture the raised Exception and assert the message is correct
        the_exception = cm.exception
        self.assertEquals("Position 1 has already been taken.", str(the_exception))

    def test_cannot_add_to_outofbounds(self):
        """
        When attempting to make a move on the board, you should not be able
        to make said play on a position that doesn't exit
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # ...I establish that I expect an InvalidPositionError to be raised
        with self.assertRaises(InvalidPositionError) as cm:
            # When...
            # ...I try to claim position 10, which doesn't exist on the board
            sub_board.claim_position(10, "X")

        # Then...
        # ...I capture the raised Exception and assert the message is correct
        the_exception = cm.exception
        self.assertEquals("Position 10 does not exist on this board.", str(the_exception))

    def test_cannot_add_to_complete_board(self):
        """
        When a board has been completed (all spaces filled), no more plays can be made
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # ...this sub-board is then completed
        fill_positions_without_win(sub_board)

        # ...I establish that I expect a BoardIsCompleteError to be raised
        with self.assertRaises(BoardIsCompleteError) as cm:
            # When...
            # ...I try to claim position 0, on a complete board
            sub_board.claim_position(0, "O")

        # Then...
        # ...I capture the raised Exception and assert the message is correct
        the_exception = cm.exception
        self.assertEquals("This board has already been completed. No more moves can be made", str(the_exception))

    def test_no_marked_winner_in_drawn_board(self):
        """
        When a board has been tied, sub_board.owner should be None
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # When...
        # ...this sub-board is then completed
        fill_positions_without_win(sub_board)

        # Then...
        # ...there should be no marked winner
        self.assertEquals(None, sub_board.get_owner())

        # And...
        # ...the board should be marked as complete
        self.assertTrue(sub_board)

    def test_player_x_is_marked_as_winner(self):
        """
        When a board has been won by player X, they should be tracked as the
        'owner' of the board
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # When...
        # ...this sub-board is won by player X
        fill_positions_with_win(sub_board, "X", "O")

        # Then...
        # ...sub_board.owner should be 'X'
        self.assertTrue(sub_board.is_board_complete())
        self.assertEqual('X', sub_board.owner)

        # And...
        # ...I establish that I expect a BoardIsCompleteError to be raised
        with self.assertRaises(BoardIsCompleteError) as cm:
            # ...I try to claim position 0, on an already won board
            sub_board.claim_position(0, "O")

        # ...I capture the raised Exception and assert the message is correct
        the_exception = cm.exception
        self.assertEqual("This board has already been won by player X", str(the_exception))

    def test_player_o_is_marked_as_winner(self):
        """
        When a board has been won by player O, they should be tracked as the
        'owner' of the board
        """
        # Given...
        # ...the sub-board is created
        sub_board = SubBoard()

        # When...
        # ...this sub-board is won by player O
        fill_positions_with_win(sub_board, "O", "X")

        # Then...
        # ...sub_board.owner should be 'O'
        self.assertTrue(sub_board.is_board_complete())
        self.assertEqual('O', sub_board.owner)

        # And...
        # ...I establish that I expect a BoardIsCompleteError to be raised
        with self.assertRaises(BoardIsCompleteError) as cm:
            # ...I try to claim position 0, on an already won board
            sub_board.claim_position(0, "X")

        # ...I capture the raised Exception and assert the message is correct
        the_exception = cm.exception
        self.assertEqual("This board has already been won by player O", str(the_exception))
