import random
from src.game.board_state import BoardState
from src.agents.player import Player

REWARD_WIN = 100
REWARD_MOVE = 0

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


class QLearning:
    def __init__(self, learning_rate=0.1, discount=0.9, epochs=100):
        QLearning.states = {}
        self.ai1 = AI(epsilon_greedy, 'x')
        self.ai2 = AI(epsilon_greedy, 'o')
        self.eta = learning_rate
        self.gamma = discount
        self.epochs = 100

    # Single game
    def epoch(self):
        game = Game([self.ai1, self.ai2])
        i = 0
        while not game.is_over():
            old_state, move, new_state = game.step()

            if game.is_over():
                reward = REWARD_WIN
            else:
                reward = REWARD_MOVE

            old_value = old_state.move_values[move[0]][move[1]]
            future = self.get_potential_future_reward(new_state)
            discount = self.gamma**i

            learned = self.eta*(reward+discount*future - old_value)
            old_state.move_values[move[0]][move[1]] = old_value + learned

            i += 1
    
    def get_potential_future_reward(self, new_state):
        return max(new_state.move_values, key=max)


    def train(self):
        for _ in range(self.epochs):
            self.epoch()
