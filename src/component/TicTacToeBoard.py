from nicegui import ui

from src.game.Board import Board


def start():
    return ui.run()


class TicTacToeBoard:

    def __init__(self):
        self.game_boards = Board(2)
        self.board = (ui
                      .element(tag='div')
                      .style("margin: 0 auto; display: grid; gap: 1rem; background-color: darkgrey; width: 50rem; height: 50rem;"))
        self.create_board_elements(self.board, self.game_boards)

    def create_board_elements(self, parent, board: Board):
        with parent:

            # Board(2)

            # Layer 0: [Board, Board, Board, Board, Board, Board, Board, Board, Board]
            # 1. call board.get_positions()
            # 2. Iterate through each, decide whether to create new div (Board) or button (None | str)
            # 2a. If creating a button, I can try using ui.button(params).bind_value(position[i])
            # 2a. If creating a button, I can also try ui.button(params, on_click)

            current_level_positions = board.get_positions()
            for i in range(0, len(current_level_positions)):
                if 3 > i:
                    x = 1
                    y = i + 1
                elif 6 > i:
                    x = 2
                    y = i - 2
                else:
                    x = 3
                    y = i - 5
                if isinstance(current_level_positions[i], Board):
                    new_sub_board = (ui.element('div')
                                     .style(f"display: grid; grid-row: {y}; grid-column: {x}; background-color: lightgrey;"))
                    self.create_board_elements(new_sub_board, current_level_positions[i])
                else:
                    button = (ui.button(on_click=lambda: button.)
                              .style(f"grid-column: {x}; grid-row: {y}; height: 5rem; width: 5rem; background-color: lightblue"))
                    with button:
                        label = (ui.label()
                                 .bind_text_from(current_level_positions[i]))
