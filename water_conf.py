from util import Stack

class Tube(Stack):
    """
    A single tube in configuration
    """
    def __init__(self, items_list):
        super().__init__()
        self.list = items_list
        self.SIZE = 4
    
    def is_full(self):
        if len(self.list) == self.SIZE:
            return True
        return False

    def top(self):
        return self.list[-1]

def print_configuration(configuration):
    for tube in configuration:
        print(tube.list)
            
class GameState: 
    """
    Specification of full game state: color water in tubes
    """
    def __init__(self, data_list):
        # A tube_list current configuration (list of stacks)
        self.configuration = [] 
        for data in data_list:
            temp = Tube(data)
            self.configuration.append(temp)
        self.cost = 0

    def get_legal_actions(self):
        actions_list = GameRules.get_legal_actions(self)
        return actions_list
    
    def get_configuration(self):
        conf = self.configuration.copy()
        return conf

    def print_configuration(self):
        for tube in self.configuration:
            print(tube.list)

class GameRules:
    """
    These functions dictate how finger interact with their environment
    """
    def get_legal_actions(state):
        """Return a list possible actions""" 
        "List tuple: source_tube, dest_tube"
        action_list = []
        conf = state.configuration
        
        for source_index in range(len(conf)):
            if conf[source_index].is_empty(): continue
            for dest_index in range(len(conf)):
                if source_index == dest_index or conf[dest_index].is_full() : 
                    continue
                if (
                    conf[dest_index].is_empty() 
                    or conf[source_index].top() == conf[dest_index].top()
                ):
                    action_list.append((source_index, dest_index))
        return action_list

class Actions:
    """
    A collection of static method for manipulating move actions
    """
    def pour_water(state, action): # legal actions
        "Get next state from action"
        # next_state = state.copy()
        # conf = next_state.configuration
        conf = state.get_configuration()
        
        source_idx = action[0]
        dest_idx = action[1]
        
        while True:
            # get item from source tube
            item = conf[source_idx].pop()
            conf[dest_idx].push(item)

            if (
                conf[source_idx].is_empty()
                or conf[dest_idx].is_full()
                or item != conf[source_idx].top()
            ): break
        return conf
        