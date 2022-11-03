import copy

class Actions:
    """
    A collection of static method for manipulating move actions
    """
    def pour_water(state, action): # legal actions
        "Get next state from action"
        # next_state = state.copy()
        # conf = next_state.config
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
        