#! /usr/bin/env python

from src.agents.human import Human
from src.game.game import Game


def main():
    game = Game([Human(), Human()])

    while not game.is_over()[0]:
        game.step()
        print(game.game_state)

if __name__ == "__main__":
    main()
