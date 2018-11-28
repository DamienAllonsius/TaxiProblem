from agent import *
from environment import *
from variables import *
from tests import * 
from UI import *
from tqdm import tqdm
import time
import numpy as np

def learn():
     # We are in the learning phase, so play = False
     play_bool = False

     # The Q function can be saved
     learn_from_file = True
     # We can load the saved Q function or start learning

     # The agent learns a good policy
     print("Learning phase...")
     for t in tqdm(range(1,ITERATION_LEARNING+1)):
          current_position = environment.get_initial_random_position()
          # At the begining the Q function has no entry, so we create one
          agent.task.first_visit_Q(current_position)
          while current_position != environment.terminal_position:
               # Only one task for the moment
               action = agent.task.act(current_position, play_bool)
               [reward, new_position] = environment.update(current_position, action)
               agent.task.updateQ(current_position, action, new_position, reward, t)
               current_position = new_position

def play(screenshots):
     play_bool = True
     agent.position = [1, 1]#environment.get_initial_random_position()
     time.sleep(0.5)
     print("Creating the User Interface...")
     user_interface = UI(environment, agent)
     user_interface.draw_all(myfont)
     frame = 0
     while agent.position != environment.terminal_position and frame < 100:
          frame += 1
          if screenshots:
               user_interface.save(frame)
          time.sleep(1)
          action = agent.task.act(agent.position, play_bool)
          [immediate_reward, new_position] = environment.update(agent.position, action)
          agent.reward += immediate_reward
          agent.position = new_position
          # We also draw the experiment with pygame librairy
          user_interface.draw_all(myfont)
          # Break the process when user presses ESCAPE
          if user_interface.key_pressed:
               break

          
time.sleep(1)

# Run tests
Tests().main()

# Initialize the data
print("Reading the environment...")
environment = Environment()
environment.init_domain(DOMAIN_SETTING)
agent = Agent(environment.get_initial_random_position())

learn()

print("Learning complete")
print("Starting experiment...")
# Now we can play with the agent
# Make the agent move in the environment until he reaches the terminal position
take_screen_shots = False
play(take_screen_shots)
