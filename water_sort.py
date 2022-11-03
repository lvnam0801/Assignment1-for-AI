from util import Stack

            
class GameState: 
    """
    Specification of full game state: color water in tubes
    """
    def __init__(self, data_list):
        # A tube_list current config (list of stacks)
        self.config = [] 
        for data in data_list:
            temp = Tube(data)
            self.config.append(temp)
        self.cost = 0

    def get_legal_actions(self):
        actions_list = GameRules.get_legal_actions(self)
        return actions_list
    
    def get_config(self):
        return self.config

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
                if WaterRules.can_pour(conf, source_index, dest_index):
                    action_list.append((source_index, dest_index))
        return action_list

class WaterRules:
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
    # def can_compare(conf, source_index, dest_index):
    #     if (conf[source_index].is_empty() or conf[source_index].get_num_of_mixed() < 2): continue

        
                

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
