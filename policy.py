"""
TODO
"""
import random
from variables import *

class Policy(object):
    """
    """
    def __init__(self, task, authorized_positions):
        self.task = task
        self.domain = authorized_positions

    def take_action(self, position):
        directions = [NORTH, SOUTH, EAST, WEST]
        return directions[random.randrange(4)]

    
    
