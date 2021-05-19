#! /usr/bin/env python

from src.game.board_state import board_to_string
from src.agents.ai import AI, QLearning, greedy
from src.agents.human import Human
from src.game.game import Game


def main():
    train()

    game = Game([AI('x', greedy), Human()])

    i = 0
    while not game.is_over()[0]:
        print()
        print(game.game_state)
        if i % 2 == 0:
            if (hash(game.game_state), 'x') in QLearning.states:
                print(QLearning.states[(hash(game.game_state), 'x')].move_values)
            else:
                print("Not found!")
        game.step()
        print()
        i += 1

    print(game.game_state)

    over,winner = game.is_over()

    if winner:
        print(game.players[game.current_player].name + " won!")
    else:
        print("Draw!")

def train():
    learning = QLearning(epochs=100000)
    learning.train()
    print(len(learning.states))
    # for key in learning.states.keys():
        # print()
        # print(key)
        # print(learning.states[key])
        # print(learning.states[key].move_values)

if __name__ == "__main__":
    main()
