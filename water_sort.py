from library import Stack
import copy

SIZE = 4
            
class GameState: 
    """
    Configuration for Water Color Sort Problem
    Specification of full game state: color water in tubes
    """
    def __init__(self, data_list):
        # A tube_list current config (list of stacks)
        self.config = [] 
        for data in data_list:
            temp = Tube(data)
            self.config.append(temp)

    def get_legal_actions(self):
        actions_list = GameRules.get_legal_actions(self)
        return actions_list

    def get_config(self):
        return self.config
    

    def print_state(self):
        for tube in self.config:
            print(tube.list)
    
    def compare(self, state_2):
        config_1 = self.get_config()
        config_2 = state_2.get_config()
        
        for idx_tube in range(len(config_1)):
            tube1 = config_1[idx_tube].list
            tube2 = config_2[idx_tube].list
            
            if len(tube1) != len(tube2):
                return False
            
            for idx_item in range(len(tube1)):
                if tube1[idx_item] != tube2[idx_item]:
                    return False
        return True

     
    def get_all_mixed_count(self):
        num_of_mixed = 0
        for tube in self.get_config():
            num_of_mixed = num_of_mixed + tube.get_num_of_mixed()
        return num_of_mixed
    
    def get_goal_mixed_count(self):
        temp = 0
        for tube in self.get_config():
            temp = temp + len(tube.list)
        temp = temp/SIZE
        return temp
    
class GameRules:
    """
    These functions dictate how finger interact with their environment
    """
    def get_legal_actions(state):
        """Return a list possible actions""" 
        "List tuple: source_tube, dest_tube"
        action_list = []
        conf = state.config
        
        for source_index in range(len(conf)):
            if (conf[source_index].is_empty()) : continue
            
            for dest_index in range(len(conf)):
                if GameRules.can_pour(conf, source_index, dest_index):
                    action_list.append((source_index, dest_index))
        return action_list
    
    def can_pour(conf, source_index, dest_index):
        if source_index == dest_index:
            return False
        elif conf[source_index].is_empty():
            return False
        elif conf[dest_index].is_full():
            return False
        elif conf[dest_index].is_empty() and conf[source_index].get_num_of_mixed() <= 1:
            return False
        elif not conf[dest_index].is_empty() and conf[source_index].top() != conf[dest_index].top():
            return False
        else:
            return True

class Tube(Stack):
    """
    A single tube in config
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

    def get_num_of_mixed(self):
        n = 0
        pre_item = 'empty'
        for item in self.list:
            if item != pre_item:
                n = n + 1
            pre_item = item
        return n

class Actions:
    """
    A collection of static method for manipulating move actions
    """
    def pour_water(state, action):
        "Get next state from action"
        next = copy.deepcopy(state)
        conf = next.get_config()
        
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
        return next