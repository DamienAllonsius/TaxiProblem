"""
This class is the environment in which the agent (here the taxi) evolves.
It is a 2D-discrete grid, which features (geometry, location of the passenger) are written in the file domain/example_domain
"""

import random
from variables import * 
class Environment(object):

    def __init__(self):
        self.reward = 0
        self.agent_position = []
        self.passenger_position = []
        self.terminal_position = []
        # TOFIX : for the moment terminal_position = passenger_position
        self.authorized_positions = []
        self.number_authorized_positions = 0
        self.init_domain()
        self.set_initial_random_position()
        
    def init_domain(self):
        """
        set the authorized_positions according to the file domain/example_domain
        set the number of authorized positions 
        set the terminal postion
        """
        file_object = open("domain/example_domain", 'r')
        i = -1
        for line in file_object.readlines():
            i += 1
            j = -1
            current_line = []
            for character in line:
                j += 1
                if character == "-":
                    current_line.append(False)
                elif character == " ":
                    current_line.append(True)
                    self.number_authorized_positions += 1
                elif character == "R":
                    current_line.append(True)
                    self.number_authorized_positions += 1
                    self.passenger_position = [j,i]
                    self.terminal_position = [j,i]
            self.authorized_positions.append(current_line)
        
    def reset(self):
        """
        restart the variables of the environment : 
        set the reward to 0
        set agent_position to a random position
        (TODO set the passenger position to their initial position)
        """
        self.reward = 0
        self.set_initial_random_position()
        
    def set_initial_random_position(self):
        """
        get a random position among the authorized positions 
        (i.e. the positions (i,j) such that self.authorized position(i,j)=True)
        We get a number between 1 and 
        number_authorized_positions - number of terminal position
        (we exclude the passengers' position at the begining)
        """
        random_position = random.randrange(1,self.number_authorized_positions - len(self.terminal_position)/2+1)
        count_true = 0
        i = -1
        for line in self.authorized_positions:
            i += 1
            j = -1
            for bool in line:
                j += 1
                # we exclude the passengers' positions
                if bool and ([j,i] not in self.terminal_position):
                    count_true += 1
                    if count_true == random_position:
                        self.agent_position = [j ,i]
                        break
        
    def update(self, action):
        """
        This method moves the taxi in direction NORTH SOUTH EAST or WEST if the target position is allowed by the domain. 
        Otherwise the Taxi get a penalty of -1 on its reward and stays at his place.
        """
        new_position = [0,0]
        for i in range(2):
            new_position[i] = self.agent_position[i] + action[i]
        if self.authorized_positions[new_position[1]][new_position[0]]:
            self.agent_position = new_position
            self.reward += REWARD_MOVE
            if self.agent_position == self.passenger_position:
                self.reward = REWARD_PASSENGER
        else:
            self.reward = REWARD_ERROR
