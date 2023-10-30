import justpy as jp


class TicTacToeBoard:

    def __init__(self):
        self.web_page = jp.WebPage()
        self.board = jp.Div(
            id="top-game-board",
            a=self.web_page,
            style="margin: 0 auto; display: grid; gap: 1rem; background-color: darkgrey; width: 50rem; height: 50rem;"
        )
        for x in range(1, 4):
            for y in range(1, 4):
                self.create_sub_board(self.board, x, y)

    def create_sub_board(self, parent_container: jp.Div, row: int, col: int):
        new_sub_board = jp.Div(
            a=parent_container,
            style=f"display: grid; grid-row: {row}; grid-column: {col}; background-color: lightgrey"
        )
        for i in range(1, 4):
            for j in range(1, 4):
                jp.Button(
                    a=new_sub_board,
                    style=f"grid-row: {i}; grid-column: {j}; height: 5rem; width: 5rem; background-color: lightblue"
                )

    def start(self):
        return self.web_page
