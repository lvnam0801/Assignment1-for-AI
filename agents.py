import search
from action import Actions

class SearchAgent(search.SearchProblem):
    """
    Agents to search goal state of Water Color
    """
    def __init__(self, game_state):
        self.game_state = game_state

    def get_start_state(self):
        return self.game_state

    def get_successor(self, state):
        successor = []
        possible_action_list = state.get_legal_actions()
        for action in possible_action_list: 
            next_state = Actions.pour_water(state, action)
            cost = self.get_cost_of_action(action)
            successor.insert(0, [next_state, action, cost])
        return successor

    def get_cost_of_action(self, actions):
        return 1     
    
    def is_goal_state(self, state):
        for tube in state.get_config():
            if tube.get_num_of_mixed() > 1:
                return False
            if len(tube.list) > 0 and len(tube.list) < 4:
                return False
        return True