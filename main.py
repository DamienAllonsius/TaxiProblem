from agent import *
from environment import *
from variables import * 
from UI import *
import time

environment = Environment() 
agent = Agent()
user_interface = UI(environment) 

# First the agent learns a good policy
for t in range(ITERATION_LEARNING):
    agent.task.learn(environment) 
    environment.reset()

# Then we can play with the agent
while environment.agent_position != environment.terminal_position:
    environment.update(agent.act(environment.agent_position))
# We also draw the situation with pygame librairy
    user_interface.draw_all()
# Break the process when user presses ESCAPE
    if user_interface.key_pressed:
        break
