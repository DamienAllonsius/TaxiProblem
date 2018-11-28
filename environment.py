"""
This class is the environment in which the agent (here the taxi) evolves.
It is a 2D-discrete grid, which features (geometry, location of the passenger) are written in the file domain/example_domain
"""
import numpy as np
from variables import *

class Environment(object):

    def __init__(self):
        """
        When the agent reaches the terminal position, the experiment ends.
        self.authorized_positions_bool contains boolean entries : 
        True : the position is allowed by the geometry of the domain
        False otherwise.
        self.authorized_positions_ij contains lists of two elements [j,i] :
        x = j, y = i is an allowed position.
        """
        self.terminal_position = []
        # TOFIX : for the moment terminal_position = passenger_position
        self.authorized_positions_bool = []
        self.authorized_positions_ij = []
        self.number_authorized_positions = 0
    
    def init_domain(self, path):
        """
        set the authorized_positions_ij and authorized_positions_bool variables  according to the file : domain/example_domain
        set the number of authorized positions
        set the terminal postion. For the moment this terminal position is the passenger's position.
        """
        number_authorized_positions = 0
        file_object = open(path, 'r')
        i = -1
        for line in file_object.readlines():
            i += 1
            j = -1
            # current_line_bool (resp. _ij) is a list of bools (resp. of positions [i,j]). It is True when the position is allowed and False otherwise. The current_line_ij contains the position of the current character if the corresponding value of current_line_bool is true.
            current_line_bool = []
            current_line_ij = []
            for character in line:
                j += 1
                if character == "-":
                    # here we are facing a wall
                    current_line_bool.append(False)
                elif character == " ":
                    # an empty space where the agent can move to
                    current_line_ij.append([i, j])
                    current_line_bool.append(True)
                    number_authorized_positions += 1
                elif character == "R":
                    # The location of the "Red" passenger
                    # There must be only 1 caracter R.
                    current_line_bool.append(True)
                    current_line_ij.append([i, j])
                    number_authorized_positions += 1
                    self.terminal_position = [i,j]
            self.authorized_positions_bool.append(current_line_bool)
            self.authorized_positions_ij += current_line_ij
            self.number_authorized_positions = number_authorized_positions
    def get_initial_random_position(self):
        """
        get a random position among the authorized positions 
        (i.e. a list [i,j] such that self.authorized_position at (i,j) is True)
        We get a number between 1 and 
        number_authorized_positions - number of terminal position
        (we exclude the passengers' position at the begining)
        """
        random_position = np.random.randint(self.number_authorized_positions - 1)
        initial_possible_positions = self.authorized_positions_ij.copy()
        initial_possible_positions.remove(self.terminal_position)
        return initial_possible_positions[random_position]                        
    def update(self, previous_position, action):
        """
        This method returns the taxi position when he takes an action NORTH SOUTH EAST or WEST and the corresponding reward.
        The agent get a penalty for every move and when he hits the wall. He gets a positive reward when reaching the passenger's location.
        """
        new_position = [0,0]
        reward = REWARD_MOVE
        for i in range(2):
            new_position[i] = previous_position[i] + action[i]
        if self.authorized_positions_bool[new_position[0]][new_position[1]]:
            if new_position == self.terminal_position:
                reward += REWARD_TERMINAL
        else:
            reward += REWARD_ERROR
            new_position = previous_position

        return [reward, new_position]
