"""
This class represents the taxi divers. He has to learn how to solve his task.
"""
import random
from variables import *
from task import *
class Agent(object):
    """
    
    """
    def __init__(self):
        self.task = Task()

        
    def act(self, position):
        """
        This function codes the policy. 
        Given a position, returns an action, which,  for the moment, can only be
        one of the DIRECTIONS.
        TODO
        """
        i = random.randrange(4)
        return DIRECTIONS[i]
