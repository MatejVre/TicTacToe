from MCTS import MCTS
from game import Game


class Controller:

    def __init__(self):
        self.game = Game()
        self.mcts = MCTS()

    def place_move(self, row, column, player):
        