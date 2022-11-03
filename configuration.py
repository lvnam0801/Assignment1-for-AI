class GameState: 
    """
    Specification of full game state: color water in tubes
    """
    def __init__(self, configuration):
        self.configuration = configuration # A tube_list current configuration
        self.cost = 0

    def get_legal_actions(self):
        GameRules.get_legal_actions(self)


class GameRules:
    
    """
    These functions dictate how finger interact with their environment
    """

    def get_legal_actions(state):
        """Return a list possible actions""" 
        "List tuple: source_tube, dest_tube"
        actions = []
        conf = state.configuration
        for source_index in len(conf):
            for dest_index in len(conf):
                if( 
                    source_index == dest_index 
                    or conf[source_index].is_empty() 
                    or conf[dest_index].is_full()
                    or conf[source_index].top() != conf[dest_index].top()
                ): 
                    continue
                else:
                    actions.append((source_index, dest_index))
        return actions

class Actions:
    """
    A collection of static method for manipulating move actions
    """
    def pour_water(state, actions): # legal actions
