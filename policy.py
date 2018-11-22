"""
TODO
"""
import random
from variables import *

class Policy(object):
    """
    """
    def __init__(self, task, authorized_positions):
        # the Q_function is a dictionnary. Keys are positions (s) and values are dictionnaries whose keys are actions (a) and values avec the value of Q(s,a).
        self.Q_function = {}
        
    def take_action(self, position):
        directions = [NORTH, SOUTH, EAST, WEST]
        return directions[random.randrange(4)]

    def find_max_action(self, dict_actions):
        # the keys of dictionnaries are always strings
        m = -float('inf')
        for d in dict_actions:
            m = max(m,dict_actions[d])
        return m 
            
    def updateQ(self,position,action,reward,learning_rate):
        # is this position has already been recorded in the Q function ?
        try:
            dict_actions = self.Q_function[str(position)]
            max_actions = self.find_max_action(dict_actions)
        except:
            # set an optimistic initial value (to encourage exploration)
            self.Q_function.update({str(position) : {str(action) : 0}})
            max_action = 0
            
        self.Q_function[position][action] *= (1 - learning_rate)
        self.Q_function[position][action] += learning_rate * (reward + max_action)

                
