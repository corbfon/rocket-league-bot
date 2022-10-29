# This file is for strategy

from util.objects import *
from util.routines import *
from random import randrange



class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
            return
        def boost_sorter(boost):
            return (self.me.location - boost.location).magnitude()
        active_boosts = [boost for boost in self.boosts if boost.active]
        active_boosts.sort(key=boost_sorter)
        self.set_intent(goto_boost(active_boosts[randrange(0, len(active_boosts) - 1)], use_boost=False))
