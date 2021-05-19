#! /usr/bin/env python

from src.game.board_state import board_to_string
from src.agents.ai import AI, QLearning, greedy
from src.agents.human import Human
from src.game.game import Game


def main():
    train()

    replay = None

    while replay != 'n':
        play()
        print()
        print("Play again? y/n")
        replay = input()


def play():
    game = Game([AI('x', greedy), Human()])

    i = 0
    while not game.is_over()[0]:
        if i % 2 == 0:
            state = QLearning.states.get((hash(game.game_state), 'x'), game.game_state)
            print(state.move_values)
        print()
        print(game.game_state)
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
    learning = QLearning(epochs=10000)
    learning.train()
    print(len(learning.states))
    # for key in learning.states.keys():
        # print()
        # print(key)
        # print(learning.states[key])
        # print(learning.states[key].move_values)

if __name__ == "__main__":
    main()
