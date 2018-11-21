"""
This class (User Interface) offers a visualisation of the Taxi moves in the domain
"""
from taxi import * 
import pygame.mixer
from pygame.locals import *
import time
pygame.init()
fontsize = 30
myfont = pygame.font.SysFont("monospace", fontsize)

class UI(object):
    """
    TODO
    """
    def __init__(self):
        self.window = pygame.display.set_mode((0,0))
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.taxi = Taxi()
        self.size_squares = 100

    def draw_targets(self):
        """
        TODO
        """
        for target in self.taxi.tasks.targets:
            pygame.draw.rect(self.window, target[1],
                         (target[0][0] * self.size_squares + self.size_squares/3,
                          target[0][1] * self.size_squares + self.size_squares/3,
                          self.size_squares/3,
                          self.size_squares/3))
    def draw_reward(self):
        """
        TODO
        """
        label = myfont.render("Reward = "+str(self.taxi.reward), 3, (255, 255, 255))                        
        self.window.blit(label, (0,0))
            
    def draw_taxi(self):
        """
        TODO
        """
        pygame.draw.circle(self.window, (0,255,0),(self.taxi.position[0] * self.size_squares + self.size_squares // 2, self.taxi.position[1]* self.size_squares + self.size_squares // 2), self.size_squares // 4)
        
    def draw_passengers(self):
        """
        TODO
        """
        for person in self.taxi.tasks.passengers:
                pygame.draw.circle(self.window, person[1],(person[0][0] * self.size_squares + self.size_squares // 2, person[0][1]* self.size_squares + self.size_squares // 2), self.size_squares // 20)

    def draw_domain_taxi(self):
        """
        TODO
        """
        cont = True
        while(cont):
            self.window.fill((0, 0, 0))
            i = -1
            for line_position in self.taxi.authorized_positions:
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
            self.taxi.play()
            self.draw_passengers()
            self.draw_taxi()
            self.draw_targets()
            self.draw_reward()
            pygame.display.flip()
            if self.taxi.position == self.taxi.tasks.targets[0][0]:
                time.sleep(2)
                cont = False
            time.sleep(1)
            
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
                        cont = False


            
