"""
The taxi has to learn (i.e. improve its policy) how to pickup passengers and bring to the right location. Finally the taxi can play with its policy. The taxi evolves in a domain defined in the file domain/example_domain. The domain is limited by '-'. Spaces characters ' ', within the rectangle defined by the border of the domain, means authorized location for the taxi and the passengers.
"""

import random
from variables import *
from tasks import *
from policy import * 

class Taxi(object):
    """ 
    This class represents a Taxi that can move in a domain and pickup passengers from a spot to another
    """
    def __init__(self, position = None):
        """
        The taxi should be initialized in an authorized position.
        """
        # for the moment we have just one task
        self.tasks = Tasks()
        self.reward = 0
        self.authorized_positions = []
        self.number_authorized_positions = 0
        self.set_authorized_positions(DOMAIN_SETTING)
        self.policy = Policy(self.tasks, self.authorized_positions)
        if position == None:
            self.set_random_position()
        else:
            assert (type(position) == list), "The position variable must be a list"
            assert (len(position) == 2), "The position variable must be a list of length 2"
            assert (self.authorized_positions[position[0]][position[1]]), "This position is not allowed by the geometry of the domain. You can omit this variable to get a random allowed position."
            self.position = position
                

            
    def learn(self):
        """
        Modify the policy. TODO
        """
        
    def play(self):
        """
        Use the policy to take action during all the process (which lasts number_of_actions)
        """
        action = self.policy.take_action(self.position)
        self.move(action)
        

    def move(self, direction):
        """
        This method moves the taxi in direction NORTH SOUTH EAST or WEST if the target position is allowed by the domain. Otherwise the Taxi get a penalty of -1 on its reward.
        """
        new_position = [0,0]
        for i in range(2):
            new_position[i] = self.position[i] + direction[i]
        if self.authorized_positions[new_position[1]][new_position[0]]:
            self.position = new_position
            # TOFIX. For the moment there is only one passenger.
            if self.position == self.tasks.passengers[0][0]:
                # The passenger is now in the taxi ! 
                self.tasks.passengers[0][2] = True
            if self.position == self.tasks.targets[0][0]:
                # The passenger is now in the taxi ! 
                self.reward += REWARD_TARGET
        else:
            self.reward += REWARD_ERROR

    def set_authorized_positions(self, path):
        """
        This method reads the file located in the variable "path". This file describes the domain with dashes : "-" and spaces : " ". The dashes represent the walls i.e. the forbidden positions whereas the spaces are the allowed positions. A position (i,j) is allowed if the variable authorized_positions[i][j] is True and forbidden otherwise. Also, sets the number of authorized positions
        """
        file_object = open(path, 'r')
        for line in file_object.readlines():
            current_line = []
            for character in line:
                if character == "-":
                    current_line.append(False)
                elif character == " " or character == "R" or character == "Y" or character == "B" or character == "T":
                    current_line.append(True)
                    self.number_authorized_positions += 1
            self.authorized_positions.append(current_line)
                
    def set_random_position(self):
        """
        Set a random position for the taxi among the authorized positions.
        """
        random_position = random.randrange(self.number_authorized_positions- len(self.tasks.passengers) - len(self.tasks.targets)) + 1
        count_true = 0
        i = -1
        # we get the passengers' positions
        people_positions = [person[0] for person in self.tasks.passengers]
        target_positions = [target[0] for target in self.tasks.targets]
        for line in self.authorized_positions:
            i += 1
            j = -1
            for bool in line:
                j += 1
                # we exclude the passengers' positions and the targets' positions
                if bool and ([j,i] not in people_positions) and ([j,i] not in people_positions): 
                    count_true += 1
                    if count_true == random_position:
                        self.position = [j ,i]
                        break
            
        
