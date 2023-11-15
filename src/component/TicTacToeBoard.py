from nicegui import ui


def start():
    return ui.run(native=True, window_size=(1920, 1080))


class TicTacToeBoard:

    def __init__(self):
        self.board = (ui
                      .element(tag='div')
                      .style("margin: 0 auto; display: grid; gap: 1rem; background-color: darkgrey; width: 50rem; height: 50rem;"))
        for x in range(1, 4):
            for y in range(1, 4):
                self.create_sub_board(x, y)

    def create_sub_board(self, row: int, col: int):
        with self.board:
            new_sub_board = (ui.element('div')
                .style(f"display: grid; grid-row: {row}; grid-column: {col}; background-color: lightgrey;"))

            with new_sub_board:
                for i in range(1, 4):
                    for j in range(1, 4):
                        (ui.button(f"[{j}, {i}]")
                         .style(f"grid-row: {i}; grid-column: {j}; height: 5rem; width: 5rem; background-color: lightblue"))
