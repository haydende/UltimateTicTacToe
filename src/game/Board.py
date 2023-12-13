from src.exception.BoardIsCompleteError import BoardIsCompleteError
from src.exception.InvalidPositionError import InvalidPositionError


class Board:

    def __init__(self, layers: int):
        self.positions: list = []
        self.board_complete: bool = False
        self.owner: str | None = None
        self.winning_combinations = \
            [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
            ]
        self.create_positions(layers)

    def is_board_complete(self):
        return self.board_complete

    def get_owner(self):
        return self.owner

    def get_positions(self):
        return self.positions

    def claim_position(self, pos: int, player_str: str):
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

        if self.has_player_won(player_str, self.winning_combinations):
            self.board_complete = True
            self.owner = player_str

    def create_positions(self, layers: int):
        """Insert n layers of Board/None values into the positions array"""
        layers = layers - 1
        if layers < 1:  # This is the final layer, where players will claim positions
            for _ in range(0, 9):
                self.positions.append(None)
        else:
            for _ in range(0, 9):  # This is another layer to contain more positions
                self.positions.append(Board(layers))

    def has_player_won(self, player_str: str, winning_combinations):
        """
        Check if the series of positions that, when equal and not None, would
        indicate that the given player has won
        :param winning_combinations: Combinations of positions that would need
        to owned by the provided player for them to claim victory
        :param player_str: Player String to check for
        :return: Boolean expression of whether the player has won the board
        """
        matched = False
        if winning_combinations:
            combo = winning_combinations[0]
            if self.positions[combo[0]] == self.positions[combo[1]] == self.positions[combo[2]] == player_str:
                matched = True
            else:
                matched = self.has_player_won(player_str, winning_combinations[1:])
        return matched

    def __eq__(self, other):
        return self.owner == other.owner
