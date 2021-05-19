import math
import random
from src.game.game import Game
from src.game.board_state import BoardState, board_to_string

REWARD_WIN = 1000
REWARD_MOVE = 0

class AI:
    def __init__(self, symbol, policy):
        self.reward = 0
        self.symbol = symbol
        self.policy = policy
        self.name = "AI"

    def get_move(self, board):
        return self.policy(board, self.symbol)

def random_policy(board_in, symbol):
    board : BoardState = QLearning.states.get((hash(board_in), symbol), board_in)
    return board.random_move()


def epsilon_greedy(board_in, symbol):
    board : BoardState = QLearning.states.get((hash(board_in), symbol), board_in)
    epsilon = 0.5

    chance = random.uniform(0, 1)

    if chance < epsilon:
        return board.random_move()
    else:
        return greedy(board, symbol)

def greedy(board_in, symbol):
    board : BoardState = QLearning.states.get((hash(board_in), symbol), board_in)
    q_values = board.move_values

    moves = board.legal_moves()
    best_move = max(moves, key=lambda x: q_values[x[0]][x[1]])
    best_val = q_values[best_move[0]][best_move[1]]
    return random.choice([x for x in moves if q_values[x[0]][x[1]] == best_val])


class QLearning:
    def __init__(self, learning_rate=0.1, discount=0.9, epochs=100):
        QLearning.states = {}
        self.ai1 = AI('x', epsilon_greedy)
        self.ai2 = AI('o', epsilon_greedy)
        self.eta = learning_rate
        self.gamma = discount
        self.epochs = epochs

    # Single game
    def epoch(self):
        game = Game([self.ai1, self.ai2])
        i = 0
        # print("NEW GAME")
        while not game.is_over()[0]:
            curr_ai = [self.ai1, self.ai2][game.current_player]
            old_state, move, new_state = game.step()
            other_ai = [self.ai1, self.ai2][game.current_player]

            # if board_to_string(old_state.board) == '_________':
                # print("yes")
                # print((hash(new_state), other_ai.symbol) in QLearning.states)


            old_state = QLearning.states.get((hash(old_state), curr_ai.symbol), old_state)
            new_state = QLearning.states.get((hash(new_state), other_ai.symbol), new_state)

            over, won = game.is_over()
            if over and won:
                reward = REWARD_WIN
            else:
                reward = REWARD_MOVE

            old_value = old_state.move_values[move[0]][move[1]]
            future = self.get_potential_future_reward(new_state)
            discount = self.gamma**i

            learned = self.eta*(reward+discount*future - old_value)
            old_state.move_values[move[0]][move[1]] = old_value + learned

            QLearning.states[(hash(old_state), curr_ai.symbol)] = old_state  

            # start_state = BoardState(board_string="_________")
            # start = QLearning.states.get((hash(start_state), 'x'), None)
            # if start is not None:
                # print(start.move_values)

            i += 1
    
    def get_potential_future_reward(self, new_state):
        return max([max(x) for x in new_state.move_values])


    def train(self):
        print("--- TRAINING ---")
        print("0% done")
        ten_percent = math.floor(self.epochs / 10)
        for i in range(self.epochs):
            if i % ten_percent == 0:
                print("{}% done".format(str(100/(self.epochs-i)*100)))
            self.epoch()
