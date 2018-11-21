"""
The tasks that the taxi can choose
"""

from variables import *

class Tasks(object):
    """
    TODO
    """
    def __init__(self):
        """
        TODO : set all the tasks here
        """
        self.passengers = []
        self.targets = []
        self.get_passengers()
        self.get_target()
        self.passenger_color = PASSENGER_COLOR
        
    def get_passengers(self):
        """
        TODO
        Passengers 3 arguments : 
        position
        color
        boolean (is he in the care or not ? At the begining : no)
        """
        file_object = open(DOMAIN_SETTING, 'r')
        i = -1
        for line in file_object.readlines():
            i += 1
            j = -1
            for character in line:
                j += 1
                if character == "R":
                    self.passengers.append([[j,i], (255,0,0), False])
                elif character == "B":
                    self.passengers.append([[j,i], (0,0,255), False])
                elif character == "Y":
                    self.passengers.append([[j,i], (255,255,0), False])    
    
        
    def get_target(self):
        """
        TODO
        """
        file_object = open(DOMAIN_SETTING, 'r')
        i = -1
        for line in file_object.readlines():
            i += 1
            j = -1
            for character in line:
                j += 1
                if character == "T":
                    self.targets.append([[j,i],(255,0,0)])
