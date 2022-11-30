# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return

        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        
        available_boosts = [boost for boost in self.boosts if boost.large and boost.active]
        closest_boost = None
        closest_distance = 10000
        for boost in available_boosts:
            distance = (self.me.location - boost.location).magnitude()
            if closest_boost is None or distance < closest_distance:
                closest_boost = boost
                closest_distance = distance
        
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            return
