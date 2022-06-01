from asyncio import constants
import random
from collections import namedtuple
import constants
from showdown.battle import Battle
from showdown.engine.damage_calculator import calculate_damage
from .monte_carlo_tree_search import MCTS, Node
from ..helpers import format_decision


_TTTB = namedtuple("PokeBoard", "")


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

    def make_move(board):
        state = board.create_state()
        my_options = board.get_all_options()[0]

        moves = []
        switches = []
        for option in my_options:
            if option.startswith(constants.SWITCH_STRING + " "):
                switches.append(option)
            else:
                moves.append(option)

        if board.force_switch or not moves:
            return format_decision(board, switches[0])

        most_damage = -1
        for move in moves:
            damage_amounts = calculate_damage(state, constants.SELF, move, constants.DO_NOTHING_MOVE)

            damage = damage_amounts[0] if damage_amounts else 0

            if damage > most_damage:
                most_damage = damage

        board.opponent.active.hp = board.opponent.active.hp - most_damage

    
    def create_tree(self):
        tree = MCTS()
        board = self
        while True:

            board = board.make_move()
            if board.is_terminal():
                return tree
            for _ in range(50):
                tree.do_rollout(board)
            board = tree.choose(board)
            print(board.to_pretty_string())
            if board.is_terminal():
                return tree


    def find_best_move(self):
        my_tree = self.create_tree()
        current_node = my_tree.choose()
        return format_decision(self, current_node)