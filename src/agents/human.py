class Human:
    def __init__(self):
        self.name = "Human"

    def get_move(self, board):
        x,y = take_input()

        if not move_in_range((x,y)) or (x,y) not in board.legal_moves():
            print("Invalid move, try again")
            return self.get_move(board)
        
        return (x,y)

def take_input():
    return [int(x) for x in input("Move: ").split()]

def move_in_range(move):
    x,y = move
    return 0 <= x <= 2 and 0 <= y <= 2

