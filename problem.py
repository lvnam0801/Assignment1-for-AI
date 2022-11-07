import water_sort
import search

SIZE = 4

class WaterProblem(search.SearchProblem):
    """
    Agents to search goal state of Water Color
    """
    def __init__(self, data):
        self.game_state = water_sort.GameState(data)

    def get_start_state(self):
        return self.game_state

    def get_successor(self, state):
        successor = []
        possible_action_list = state.get_legal_actions()
        for action in possible_action_list: 
            next_state = water_sort.Actions.pour_water(state, action)
            cost = self.get_cost_of_action(action)
            successor.insert(0, [next_state, action, cost])
        return successor

    def get_cost_of_action(self, action):
        return 1     
    
    def is_goal_state(self, state):
        for tube in state.get_config():
            if tube.get_num_of_mixed() > 1:
                return False
            if len(tube.list) > 0 and len(tube.list) < SIZE:
                return False
        return True
    
    def get_all_mixed_count(self, state):
        num_of_mixed = 0
        for tube in state.get_config():
            num_of_mixed = num_of_mixed + tube.get_num_of_mixed()
        return num_of_mixed
    
    def get_goal_mixed_count(self, state):
        temp = 0
        for tube in state.get_config():
            temp = temp + len(tube.list)
        temp = temp/SIZE
        return temp