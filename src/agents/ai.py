import math
import random
from src.game.game import Game
from src.game.board_state import BoardState

REWARD_WIN = 1
REWARD_LOSE = -1
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
    epsilon = 0.3

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
        last_old_state = None
        last_move = None
        
        while not game.is_over()[0]:
            curr_ai = [self.ai1, self.ai2][game.current_player]

            old_state, move, new_state = game.step()
            other_ai = [self.ai1, self.ai2][game.current_player]

            old_state = QLearning.states.get((hash(old_state), curr_ai.symbol), old_state)
            new_state = QLearning.states.get((hash(new_state), other_ai.symbol), new_state)


            over, won = game.is_over()
            if over and won:
                reward_curr = REWARD_WIN
                reward_other = REWARD_LOSE
            else:
                reward_curr = REWARD_MOVE
                reward_other = REWARD_MOVE

            self.update_player(old_state, move, new_state, curr_ai.symbol, reward_curr, i)

            if last_old_state != None and last_move != None:
                self.update_player(last_old_state, last_move, None, other_ai.symbol, reward_other, i-1)

            
            last_old_state = old_state
            last_move = move

            # print("Reward first")
            # print(reward_curr)
            # print("Reward last")
            # print(reward_other)
            # print("New")
            # print(new_state.move_values)
            # print()

            i += 1

    def update_player(self, old_state, move, new_state, symbol, reward, discount_exp):
        if new_state == None:
            future = 0
        else:
            future = self.get_potential_future_reward(new_state)
        old_value = old_state.move_values[move[0]][move[1]]
        discount = self.gamma**discount_exp

        learned = self.eta*(reward+discount*future - old_value)
        old_state.move_values[move[0]][move[1]] = old_value + learned

        QLearning.states[(hash(old_state), symbol)] = old_state  
    
    def get_potential_future_reward(self, new_state):
        return max([max(x) for x in new_state.move_values])


    def train(self):
        print("--- TRAINING ---")
        ten_percent = math.floor(self.epochs / 10)
        for i in range(self.epochs):
            if ten_percent > 0 and i % ten_percent == 0:
                print("{} / {} epochs".format(i, self.epochs))
            self.epoch()
        print("--- TRAINING DONE ---")

