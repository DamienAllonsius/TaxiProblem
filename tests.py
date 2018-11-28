from environment import *
from agent import *
class Tests:
    """
    A bunch of functions to test the program
    """
    def __init__(self):
        self.environment = Environment()
        

    def main(self):
        #Run the test functions
        b=self.tests()
        
        #If the tests passes then
        if b:
            print("All tests are OK")
            print("Main is now running")
        else:
            print("WARNING TEST FAILURE")
        return b
    
        
        
    def tests(self):
        """
        Launch the tests
        #Input 
        NULL
        #Output
        boolean
        """
        b = True
        b *= self.test_init_domain()
        b *= self.get_initial_random_position()
        b *= self.test_update_environment()
        b *= self.test_act()
        b *= self.test_update_Q()
        return b

    def test_init_domain(self):
        self.environment.init_domain("domain/test_domain")
        answer_authorized_positions_bool = [[False, False, False, False, False], [False, True, True , True, False], [False, False, False, True, False], [False, False, False, False, False]]
        answer_authorized_positions_ij = [[1, 1], [1, 2], [1, 3], [2, 3]]
        answer_number_authorized_positions = 4

        if answer_authorized_positions_bool != self.environment.authorized_positions_bool:
            print("TEST test_init_domain FAILURE. \n authorized_positions_bool is wrong.")
            return False
        if answer_authorized_positions_ij != self.environment.authorized_positions_ij:
            print("TEST test_init_domain FAILURE. \n authorized_positions_ij is wrong.")
            print(self.environment.authorized_positions_ij)
            return False
        if answer_number_authorized_positions != self.environment.number_authorized_positions:
            print("TEST test_init_domain FAILURE. \n Number of authorized_position is wrong.")
            return False
        if self.environment.terminal_position != [1, 3]:
            print("TEST test_init_domain FAILURE. \n terminal_position is wrong.")
            return False
        return True
            
    def get_initial_random_position(self):
        self.environment.init_domain("domain/test_domain")
        answer_initial_position = [[1, 1], [1, 2], [2, 3]]
        for k in range(50):
            initial_position = self.environment.get_initial_random_position()
            if initial_position not in answer_initial_position:
                print("TEST get_initial_random_position FAILURE")
                return False
        return True

    def test_update_environment(self):
        path = [[2, 3], [1, 3], [1, 2], [1, 1]]
        path_next = [[1, 3], [1, 2], [1, 1], [1, 1]]
        rewards = [REWARD_MOVE + REWARD_TERMINAL, REWARD_MOVE, REWARD_MOVE,  REWARD_ERROR + REWARD_MOVE]
        actions = [NORTH, WEST, WEST, WEST]
        for i in range(4):
            if [rewards[i],path_next[i]] != self.environment.update(path[i], actions[i]):
                print(i)
                print([rewards[i],path_next[i]])
                print(self.environment.update(path[i], actions[i]))
                print("TEST test_update_environment FAILURE")
                return False
        return True

    def test_act(self):
        agent = Agent(self.environment.get_initial_random_position())
        agent.task.Q_function = {'[1,2]' : {'NORTH' : 0, 'SOUTH' : 100, '"EAST"' : -45, 'WEST' : 1}, '[4,7]' : {'NORTH' : 0, 'SOUTH' : 0, '"EAST"' : 0, 'WEST' : 1}, '[2,5]' : {'NORTH' : -1, 'SOUTH' : 1, '"EAST"' : -4, 'WEST' : 1000} }

        if agent.task.act('[1,2]', True) != SOUTH or agent.task.act('[2,5]', True) != WEST:
            print("TEST test_act FAILURE")
            return False
        return True

    def test_update_Q(self):
        agent_0 = Agent([4,2])
        current_position = agent_0.position
        agent_0.task.first_visit_Q(current_position)
        answer_Q = {'[4, 2]': {str(SOUTH): 0, str(NORTH): 0, str(WEST): 0, str(EAST): 0}}
        if agent_0.task.Q_function != answer_Q:
            print("TEST_0 test_update FAILURE")
            return False
        
        agent = Agent(self.environment.get_initial_random_position())
        agent.task.updateQ([5,12], NORTH, [0,0], REWARD_ERROR, 2)
                
        answer_Q = {'[0, 0]': {str(SOUTH): 0, str(NORTH): 0, str(WEST): 0, str(EAST): 0}, '[5, 12]': {str(SOUTH): 0, str(NORTH): 0, str(WEST): 0, str(EAST): 0}}
        if agent.task.Q_function != answer_Q:
            print("TEST_1 test_update FAILURE")
            return False
        agent.task.updateQ([5,12], NORTH, [0,0], REWARD_ERROR, 6)
        answer_Q = {'[0, 0]': {str(SOUTH): 0, str(NORTH): 0, str(WEST): 0, str(EAST): 0}, '[5, 12]': {str(SOUTH): 0, str(NORTH): 1 / 6 * REWARD_ERROR, str(WEST): 0, str(EAST): 0}}
        if agent.task.Q_function != answer_Q:
            print("TEST_2 test_update FAILURE")
            return False
        return True
