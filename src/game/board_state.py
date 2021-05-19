from random import randrange
from typing import List


class BoardState:
    def __init__(self, board_array=None, board_string=None):
        if board_array != None:
            self.board = board_array

        elif board_string != None:
            self.board = string_to_board(board_string)
        else:
            self.board = string_to_board("         ")
        self.move_values = build_move_values()


    def __str__(self) -> str:
        symbols = []
        for row in self.board:
            for symbol in row:
                symbols.append(symbol)
            symbols.append("\n")
        return "".join(symbols).rstrip()

    def legal_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i,j))

        return moves

    def random_move(self):
        moves = self.legal_moves()
        random_index = randrange(len(moves))
        return moves[random_index]

    def execute_move(self, move, player_num):
        symbol = ['x', 'o'][player_num]
        x,y = move
        self.board[x][y] = symbol

    def is_over(self, last_player_num):
        board = self.board
        symbol = ['x', 'o'][last_player_num]

        # Rows
        for i in range(3):
            test = [x == symbol for x in [board[i][0], board[i][1], board[i][2]]]
            if all(test):
                return True
        # Columns
        for i in range(3):
            test = [x == symbol for x in [board[0][i], board[1][i], board[2][i]]]
            if all(test):
                return True

        # Diagonals, left-right, right-left
        diagonal1 = [x == symbol for x in [board[0][0], board[1][1], board[2][2]]]
        diagonal2 = [x == symbol for x in [board[2][0], board[1][1], board[0][2]]]

        if all(diagonal1) or all(diagonal2):
            return True

        # No row, column or diagonal is complete
        return False

    def __hash__(self) -> int:
        string = board_to_string(self.board)
        return hash(string)
        




def board_to_string(board) -> str:
    symbols = []
    for row in board:
        for symbol in row:
            symbols.append(symbol)
    return "".join(symbols)

def string_to_board(string):
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(string[(i*3)+j])
        board.append(row)
    return board

def build_move_values() -> list[list[int]]:
    return [[0]*3 for _ in range(3)]

# test = BoardState(board_string="   x oxxx")
# print(test)
# test2 = build_move_values()
# test2[1][2] = 1
# print(test2)

# test = BoardState(board_string="   x oxox")
# print(test)
# print(test.is_over(0))

