# Steps through a game of Tic-Tac-Toe

from src.game.board_state import BoardState


class Game:
    def __init__(self, players) -> None:
        self.players = players
        self.game_state = BoardState()
        self.current_player = 0

    def step(self):
        old_state = self.game_state
        move = self.players[self.current_player].get_move(self.game_state)
        self.game_state.execute_move(move, self.current_player)
        new_state = self.game_state

        if not self.is_over():
            self.switch_player()

        return old_state,move,new_state



    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2

    def is_over(self):
        return self.game_state.is_over(self.current_player)

    def get_current_player(self):
        return self.current_player
