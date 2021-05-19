#! /usr/bin/env python

from src.agents.human import Human
from src.game.game import Game


def main():
    replay = None

    while replay != 'n':
        play()
        print()
        print("Play again? y/n")
        replay = input()

def play():
    game = Game([Human(), Human()])

    print("--- HUMAN VS HUMAN ---")
    while not game.is_over()[0]:
        print()
        print(game.game_state)
        game.step()
        print()

    print(game.game_state)
    print()

    over,winner = game.is_over()

    if winner:
        print(game.players[game.current_player].name + " " + str((game.current_player + 1)) + " won!")
    else:
        print("Draw!")



if __name__ == "__main__":
    main()
