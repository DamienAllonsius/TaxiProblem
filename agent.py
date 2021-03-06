"""
This class represents the taxi divers. He has to learn how to solve his tasks. This class is essentially empty for the moment because their is only one task and no hierarchy for the moment.
"""
from task import *
class Agent(object):
    """
    The agent has to learn a task and apply the best action he can
    """
    def __init__(self, position):
        self.task = Task()
        self.reward = 0
        self.position = position

    def learn_task(self):
        """
        The agent learns the only tasks he has for the moment.
        TODO make a function : learn_all_tasks
        """
        return self.task.learn()

    def save_learned_task(self, path_file):
        """
        Save the Q function in the file : path_file
        """
        f = open(path_file, 'w' )
        f.write('dict = ' + repr(self.Q_function) + '\n' )
        f.close()
    
