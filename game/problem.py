import game.water_sort as water_sort
import game.bloxorz as bloxorz
import library.search as search



class WaterProblem(search.SearchProblem):
    """
    Agents to search goal state of Water Color
    """
    
    def __init__(self, data):
        self.game_state = water_sort.GameState(data)

    def get_start_state(self):
        return self.game_state
    
    def is_goal_state(self, state):
        for tube in state.get_config():
            if tube.get_num_of_mixed() > 1:
                return False
            if len(tube.list) > 0 and len(tube.list) < water_sort.SIZE:
                return False
        return True

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
    
    def heuristic(self, state):
        h_cost = state.get_all_mixed_count() - state.get_goal_mixed_count()
        return h_cost
   
class BloxorzProblem(search.SearchProblem):
    """
    Implement interface problem for BLOXORZ problem
    """
    def __init__(self, data):
        self.game_state = bloxorz.GameState(data[0], data[1])
        self.goal_state = bloxorz.GameState(data[0], data[2])
        self.get_successor(self.goal_state)

    def get_start_state(self):
        return self.game_state
    
    def is_goal_state(self, state):
        if(state.get_config() == self.goal_state.get_config()):
            return True
        return False

    def get_successor(self, state):
        successor = []
        action_list = state.get_legal_actions()
        for action in action_list:
            next_state = bloxorz.Action.move(state, action)
            cost = self.get_cost_of_action(action)
            successor.insert(0, [next_state, action, cost])

        return successor

    def get_cost_of_action(self, action):
        """
        Actions: a list of actions to take
        This method retur total cost of a particular sequence of actions. The sequence must be composed of legal moves.
        """
        return 1