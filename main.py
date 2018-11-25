from agent import *
from environment import *
from variables import *
from tests import * 
from UI import *
import time

# Run tests
Tests().main()

# Initialize the data
environment = Environment()
environment.init_domain("domain/example_domain")
print("Reading the environment...")
agent = Agent(environment.get_initial_random_position())
print("Initializing the initial position...")

# The agent learns a good policy
print("Learning phase...")
for t in range(1,ITERATION_LEARNING+1):
     current_position = environment.get_initial_random_position()
     # At the begining the Q function has no entry, so we create one
     agent.task.first_visit_Q(current_position)

     while current_position != environment.terminal_position:
         # Only one task for the moment
         action = agent.task.act(current_position)
         [reward, new_position] = environment.update(current_position, action)
         agent.task.updateQ(current_position, action, new_position, reward, t)
         current_position = new_position

print("Learning complete")
print("Starting experiment...")
# Now we can play with the agent
# Make the agent move in the environment until he reaches the terminal position
agent.position = environment.get_initial_random_position()
time.sleep(0.5)
print("Creating the User Interface...")
user_interface = UI(environment, agent)

while agent.position != environment.terminal_position:
    time.sleep(1)
    action = agent.task.act(agent.position)
    [immediate_reward, new_position] = environment.update(agent.position, action)
    agent.reward += immediate_reward
    agent.position = new_position
    # We also draw the experiment with pygame librairy
    user_interface.draw_all(myfont)
    # Break the process when user presses ESCAPE
    if user_interface.key_pressed:
        break
     
time.sleep(2)
