# Q-learning Tic-tac-toe
A Python Tic-Tac-Toe game with an AI opponent that learns how to play via 
Q-learning (Reinforcement learning).

### Usage

There are three scripts in the root repository, `human-vs-ai.py`, `human-vs-human.py` and
`train-only.py`. These are pretty self-explanitory. `human-vs-ai.py` is the main way of
playing against the AI, this script first trains the AI by letting two AI's play against
each other for 10000 games (modifiable), then lets you play against the AI.

You can also use `human-vs-human.py` for playing with two humans, but this was mostly used
for testing purposes, and is not really the point of this repo.


### The learning process

The AI learns via a pretty standard Q-learning algorithm. The following is the rewards
given for each action done by an AI:

```
WIN: 1
LOSE: -1
MOVE: 0
```

Since the AI learns by playing against itself, the code can be a bit unclean at certain
points, this is because the two AI's need to learn from each others wins and losses. This
was something I realised too late.
