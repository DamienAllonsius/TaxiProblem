"""
This is the User Interface where we draw the environment.
We use pygame for that.
"""
import pygame.mixer
from variables import * 
from pygame.locals import *
import time

pygame.init()
myfont = pygame.font.SysFont("monospace", FONTSIZE)

class UI(object):
    """
    The main function of this class is draw_all
    The taxi is the big green circle
    The target is the red small circle
    TODO : include the target (square of the same color as the passenger)
    """
    def __init__(self, environment, agent):
        self.agent = agent
        self.environment = environment
        self.window = pygame.display.set_mode([600,500])
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.size_squares = 40
        self.key_pressed = False

    def draw_reward_label(self, myfont):
        """
        This function draws the current reward of the Agent
        """
        label = myfont.render("Reward = "+str(self.agent.reward), 3, (255, 255, 255))                        
        self.window.blit(label, (0,0))
            
    def draw_taxi(self):
        """
        This function draws the taxi as a green circle
        """
        pygame.draw.circle(self.window, (0,255,0),(self.agent.position[1] * self.size_squares + self.size_squares // 2, self.agent.position[0]* self.size_squares + self.size_squares // 2), self.size_squares // 4)
        
    def draw_passengers(self):
        """
        This function draws the passenger on the grid as a red circle.
        The location of the passenger is coded in the file domain/example_domain with the character R
        TODO : add more passengers
        """
        pygame.draw.circle(self.window, (255,0,0) ,(self.environment.terminal_position[1] * self.size_squares + self.size_squares // 2, self.environment.terminal_position[0]* self.size_squares + self.size_squares // 2), self.size_squares // 10)

    def draw_grid(self):
        """
        Draw the grid : white squares when the positions are allowed
        """
        for [i,j] in self.environment.authorized_positions_ij:
            pygame.draw.rect(self.window, (255,255,255),
                             (j * self.size_squares,
                              i * self.size_squares,
                              self.size_squares,
                              self.size_squares),1)
    def draw_all(self, myfont):
        """
        this function draws all the components of the environment:
        the domain
        the passenger
        the taxi
        and write the reward
        """

        # First draw the square representing the grid
       
        # Then draw the components of the environment
        self.window.fill((0, 0, 0))
        self.draw_grid()
        self.draw_passengers()
        self.draw_taxi()
        self.draw_reward_label(myfont)
        pygame.display.flip()

        # Exit the UI when key ESCAPE is pressed
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.key_pressed = True

    def save(self, frame):
        pygame.image.save(self.window, "screenshots/screenshot" + str(frame) + ".jpeg")
            



    
