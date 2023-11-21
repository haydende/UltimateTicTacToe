
from abc import abstractmethod


class Board:

    def __init__(self):
        self.positions: list = []
        self.board_complete: bool = False
        self.owner: str | None = None

    def is_board_complete(self):
        return self.board_complete

    def get_owner(self):
        return self.owner

    @abstractmethod
    def create_positions(self):
        pass

    @abstractmethod
    def has_player_won(self, player_str: str):
        pass
