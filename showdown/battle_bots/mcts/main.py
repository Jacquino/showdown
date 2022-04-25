import math
import random
from abc import ABC, abstractmethod
from collections import defaultdict, namedtuple

from showdown.battle import Battle
from .monte_carlo_tree_search import Node
from ..helpers import format_decision


_TTTB = namedtuple("TicTacToeBoard", "tup turn winner terminal")


class BattleBot(Battle, Node):
    def __init__(self, *args, **kwargs):
        super(BattleBot, self).__init__(*args, **kwargs)

    def find_children(board):
        return {
            board.get_all_options()
        }

    def find_random_child(board):
        return random.choice(board.get_all_options())

    def reward(board):
        if len(board.user.reserve) == 0:
            return 0
        else:
            return 1

    def is_terminal(board):
        return len(board.user.reserve) == 0 or len(board.opponent.reserve) == 0

    def make_move(board, index):
        #I don't control the parti I can just send my choice tout the server and wait her response

    def to_pretty_string(board):

    def find_best_move(self):
        my_options = self.get_all_options()[0]
        return format_decision(self, random.choice(my_options))