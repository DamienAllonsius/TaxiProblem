"""
This is the User Interface where we draw the environment.
We use pygame for that.
"""
import pygame.mixer
from pygame.locals import *
import time
pygame.init()
fontsize = 30
myfont = pygame.font.SysFont("monospace", fontsize)

class UI(object):
    """
    The main function of this class is draw_all
    The taxi is the big green circle
    The target is the red small circle
    TODO : include the target (square of the same color as the passenger)
    """
    def __init__(self, environment):
        self.environment = environment
        self.window = pygame.display.set_mode((0,0))
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.size_squares = 100
        self.key_pressed = False

    def draw_reward_label(self):
        """
        This function draws the current reward of the Agent
        """
        label = myfont.render("Reward = "+str(self.environment.reward), 3, (255, 255, 255))                        
        self.window.blit(label, (0,0))
            
    def draw_taxi(self):
        """
        This function draws the taxi as a green circle
        """
        pygame.draw.circle(self.window, (0,255,0),(self.environment.agent_position[0] * self.size_squares + self.size_squares // 2, self.environment.agent_position[1]* self.size_squares + self.size_squares // 2), self.size_squares // 4)
        
    def draw_passengers(self):
        """
        This function draws the passenger on the grid as a red circle.
        The location of the passenger is coded in the file domain/example_domain with the character R
        TODO : add more passengers
        """
        pygame.draw.circle(self.window, (255,0,0) ,(self.environment.passenger_position[0] * self.size_squares + self.size_squares // 2, self.environment.passenger_position[1]* self.size_squares + self.size_squares // 2), self.size_squares // 20)

    def draw_all(self):
        """
        this function draws all the components of the environment:
        the domain
        the passenger
        the taxi
        and write the reward
        """

        # First draw the square representing the grid
        self.window.fill((0, 0, 0))
        i = -1
        for line_position in self.environment.authorized_positions:
            i += 1
            j = -1
            for position in line_position:
                j += 1
                if position:
                    pygame.draw.rect(self.window, (255,255,255),
                                     (j * self.size_squares,
                                      i * self.size_squares,
                                      self.size_squares,
                                      self.size_squares),1)
        # Then draw the components of the environment
        self.draw_passengers()
        self.draw_taxi()
        self.draw_reward_label()
        pygame.display.flip()


        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                    # if (event.key == K_UP):
                    #     self.taxi.move(NORTH)
                    # if (event.key == K_DOWN):
                    #     self.taxi.move(SOUTH)
                    # if (event.key == K_LEFT):
                    #     self.taxi.move(WEST)
                    # if (event.key == K_RIGHT):
                    #     self.taxi.move(EAST)
                if (event.key == pygame.K_ESCAPE):
                    self.key_pressed = True


            



    
