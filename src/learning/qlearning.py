from src.game.board_state import string_to_board
from src.game.game import Game
from src.agents.ai import AI, epsilon_greedy

REWARD_WIN = 100
REWARD_MOVE = 0

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
