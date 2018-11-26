"""
This class represents a task for the taxi driver.
For the moment, the only task available is : 
Go to the (unique) passenger.
"""
from variables import *

class Task(object):
    """
    The task needs an environment to take actions 
    """
    def __init__(self):
        self.Q_function = {}

    def init_Q_function(self):
        """
        Set all the values of the Q_function to zero : 
        forall s,a, Q(s,a) = 0
        """
        for d in self.environment.authorized_positions_ij:
            self.Q_function.update({str(d) : {"NORTH" : 0, "SOUTH" : 0, "EAST" : 0, "WEST" : 0}})

    def first_visit_Q(self, position):
        known_state_action = True
        # If Q(current_position,action) does not exist, initialize.
        try:
            self.Q_function[str(position)]
        except:
            self.Q_function.update({str(position) : {str(NORTH) : 0, str(SOUTH) : 0, str(EAST) : 0, str(WEST) : 0}})
            known_state_action = False
        return known_state_action

                
    def updateQ(self, current_position, action, new_position, reward, t):
        """
        Q learning procedure : 
        Q_{t+1}(current_position, action) = 
        (1- learning_rate) * Q_t(current_position, action)
        + learning_rate * [reward + max_{actions} Q_(new_position, action)
        """
        Q_knows_current_position = self.first_visit_Q(current_position)
        Q_knows_new_position =  self.first_visit_Q(new_position)
        
        if Q_knows_current_position:
            learning_rate = 1 / t
            # TOFIX
            if Q_knows_new_position:
                dict_actions = self.Q_function[str(new_position)]
                max_action = self.find_max_action(dict_actions)
                max_value_action = dict_actions[str(max_action)]
            else:
                max_value_action = 0
            # update the Q function with Q Learning algorithme
            self.Q_function[str(current_position)][str(action)] *= (1 - learning_rate)
            self.Q_function[str(current_position)][str(action)] += learning_rate * (reward + max_value_action)
    
    def act(self, position):
        """
        This function codes the output of the policy. 
        Given a position, returns an action, which, for the moment, can only be one of the DIRECTIONS. The action is chosen as follow:
        action = argmax_{a} Q(current_position,a)
        TODO : hierarchical learning
        """
        return self.find_max_action(self.Q_function[str(position)])
    
    def find_max_action(self, dict_actions):
        """
        Take the maximum over all dictionnary's actions dict_actions.
        N.B : the dictionnaries' keys are always strings
        return argmax_{action} dict_actions
        """
        m = -float('inf')
        action = None
        for d in dict_actions:
            if dict_actions[d] > m:
                action = d
                m = max(m,dict_actions[d])
        return eval(action)


    
    def save_learned_task(self, path_file):
        """
        Save the Q function in the file path_file
        """
        f = open(path_file, 'w' )
        f.write('Q_function = ' + repr(self.Q_function) + '\n' )
        f.close()
    
