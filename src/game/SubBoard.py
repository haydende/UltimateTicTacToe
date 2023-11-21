from src.exception.BoardIsCompleteError import BoardIsCompleteError
from src.exception.InvalidPositionError import InvalidPositionError
from src.game.Board import Board


class SubBoard(Board):

    def __init__(self):
        super().__init__()
        self.create_positions()

    def create_positions(self):
        for _ in range(0, 9):
            self.positions.append(None)

    def claim_position(self, pos: int, player_str: str):
        """
        Attempt to claim the provided position as the provided player
        :param pos: position on this board
        :param player_str: player string to mark the position with
        """
        if self.board_complete:
            exception_message = "This board has already been completed. No more moves can be made"
            if self.owner is not None:
                exception_message = f"This board has already been won by player {self.owner}"
            raise BoardIsCompleteError(exception_message)
        if 0 < pos > 8:
            raise InvalidPositionError(f"Position {pos} does not exist on this board.")
        if self.positions[pos] is not None:
            raise InvalidPositionError(f"Position {pos} has already been taken.")

        self.positions[pos] = player_str

        if self.positions.count(None) == 0:
            self.board_complete = True

        if self.has_player_won(player_str):
            self.board_complete = True
            self.owner = player_str

    def has_player_won(self, player_str: str):
        """
        Check if the series of positions that, when of the same value
        (that isn't None), would indicate that the given player has won
        :param player_str: Player String to check for
        :return: Boolean expression of whether the player has won the board
        """
        if (self.positions[0] == self.positions[1] == self.positions[2] == player_str) or \
           (self.positions[3] == self.positions[4] == self.positions[5] == player_str) or \
           (self.positions[6] == self.positions[7] == self.positions[8] == player_str) or \
           (self.positions[0] == self.positions[3] == self.positions[6] == player_str) or \
           (self.positions[1] == self.positions[4] == self.positions[7] == player_str) or \
           (self.positions[2] == self.positions[5] == self.positions[8] == player_str) or \
           (self.positions[0] == self.positions[4] == self.positions[8] == player_str) or \
           (self.positions[2] == self.positions[4] == self.positions[6] == player_str):
            return True
