# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        self.print_debug()
        if self.get_intent() is not None:
            self.debug_intent()
            return
        if self.kickoff_flag:
            self.clear_debug_lines()
            self.set_intent(kickoff())
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            return
        
        self.clear_debug_lines()
        if self.is_in_front_of_ball():
            retreat_location = self.friend_goal.location
            self.set_intent(goto(retreat_location))
            self.debug_text = 'retreating'
            self.add_debug_line('retreat', self.me.location, retreat_location, [255, 0, 0])
            return

        if self.me.boost > 99:
            shot_location = self.foe_goal.location
            self.set_intent(short_shot(shot_location))
            self.debug_text = 'shooting'
            self.add_debug_line('me_to_ball', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('ball_to_net', self.ball.location, shot_location, [0, 0, 255])
            return
    
        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            boost_location = target_boost.location
            self.set_intent(goto(boost_location))
            self.debug_text = 'getting boost'
            self.add_debug_line('getting boost', self.me.location, boost_location, [0, 255, 0])
            return
