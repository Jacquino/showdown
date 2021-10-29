import random
from showdown.battle import Battle
from ..helpers import format_decision


class BattleBot(Battle):
    def __init__(self, *args, **kwargs):
        super(BattleBot, self).__init__(*args, **kwargs)

    def find_best_move(self):
        my_options = self.get_all_options()[0]
        return format_decision(self, random.choice(my_options))