#! /usr/bin/env python

from src.agents.ai import QLearning


def main():
    qlearning = QLearning(epochs=10000)
    qlearning.train()

if __name__ == "__main__":
    main()
