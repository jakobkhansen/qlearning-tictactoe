#! /usr/bin/env python

from src.game.board_state import board_to_string
from src.agents.ai import AI, QLearning, greedy
from src.agents.human import Human
from src.game.game import Game

EPOCHS=10000

def main():
    train()

    replay = None

    while replay != 'n':
        play()
        print()
        print("Play again? y/n")
        replay = input()


def play():
    game = Game([Human(), AI('o', greedy)])

    print("--- HUMAN VS AI ---")
    while not game.is_over()[0]:
        print()
        print(game.game_state)
        game.step()
        print()

    print(game.game_state)
    print()

    over,winner = game.is_over()

    if winner:
        print(game.players[game.current_player].name + " won!")
    else:
        print("Draw!")


def train():
    learning = QLearning(epochs=EPOCHS)
    learning.train()
    # for key in learning.states.keys():
        # print()
        # print(key)
        # print(learning.states[key])
        # print(learning.states[key].move_values)

if __name__ == "__main__":
    main()
