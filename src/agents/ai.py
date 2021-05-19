import random
from src.game.board_state import BoardState, string_to_board

from src.learning.qlearning import QLearning
from src.agents.player import Player


class AI(Player):
    def __init__(self, symbol, policy):
        super().__init__()
        self.reward = 0
        self.symbol = symbol
        self.policy = policy

    def get_move(self, board):
        return self.policy(board, self.symbol)

def epsilon_greedy(board_in, symbol):
    board : BoardState = QLearning.states.get((board_in, symbol), BoardState(board_in))
    epsilon = 0.1

    chance = random.uniform(0, 1)

    if chance < epsilon:
        return board.random_move()
    else:
        return greedy(board, symbol)

def greedy(board_in, symbol):
    board : BoardState = QLearning.states.get((board_in, symbol), BoardState(board_in))
    q_values = board.move_values

    moves = board.legal_moves()
    best_move = max(moves, key=lambda x: q_values[x[0]][x[1]])
    return best_move
