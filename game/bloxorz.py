import copy

class GameState:
    """
    Configuration for Bloxor
    """
    def __init__(self, map, block_config):
        self.map = map
        self.block_config = block_config
    
    def get_map(self):
        return self.map
    
    def get_config(self):
        return self.block_config

    def get_legal_actions(self):
        action_list = GameRule.get_legal_actions(self)
        return action_list
    
    def compare(self, state_2):
        if self.get_config() == state_2.get_config():
            return True
        return False

    def print_state(self):
        map_copy =  copy.deepcopy(self.map)
        map_copy[self.block_config[0][0]][self.block_config[0][1]] = 8
        map_copy[self.block_config[1][0]][self.block_config[1][1]] = 8
        for row in map_copy:
            print(row)
    
class GameRule:
    """
    Rules of game state
    """
    def get_legal_actions(state):
        """
        Block can move UP, DOWN, LEFT, RIGHT in at the state
        """
        action_list = []
        map = state.get_map()
        block_config =  state.get_config()
        
        if GameRule.check_move_up(map, block_config):
            action_list.append(Action.UP)
        if GameRule.check_move_down(map, block_config):
            action_list.append(Action.DOWN)
        if GameRule.check_move_left(map, block_config):
            action_list.append(Action.LEFT)
        if GameRule.check_move_right(map, block_config):
            action_list.append(Action.RIGHT)
        
        return action_list

    def check_move_up(map, block_config):
        next_conf = Action.move_up(map, block_config)
        if GameRule.check_legal_position(map, next_conf):
            return True
        return False

    def check_move_down(map, block_config):
        next_conf = Action.move_down(map, block_config)
        if GameRule.check_legal_position(map, next_conf):
            return True
        return False
    
    def check_move_left(map, block_config):
        next_conf = Action.move_left(map, block_config)
        if GameRule.check_legal_position(map, next_conf):
            return True
        return False
 
    def check_move_right(map, block_config):
        next_conf = Action.move_right(map, block_config)
        if GameRule.check_legal_position(map, next_conf):
            return True
        return False
    
    def check_legal_position(map, next_conf):
        """
        Out of rank or the position is equal zero
        """
        # get position
        next_position_1 = next_conf[0]
        next_position_2 = next_conf[1]


        # check out of map range
        max_idx_row = len(map) - 1
        max_idx_column = len(map[0]) - 1

        if next_position_1[0] < 0 or next_position_1[0] > max_idx_row:
            return False
        if next_position_1[1] < 0 or next_position_1[1] > max_idx_column:
            return False
        if next_position_2[0] < 0 or next_position_2[0] > max_idx_row:
            return False
        if next_position_2[1] < 0  or next_position_2[1] > max_idx_column:
            return False
        
        # check next position is not equal zeros
        if map[next_position_1[0]][next_position_1[1]] == 0:
            return False
        if map[next_position_2[0]][next_position_2[1]] == 0:
            return False
        
        return True
        
class Action:
    """
    ACTION OF BLOCK: UP, DOWN, LEFT, RIGHT
    """
    
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'

    def move(state, action):
        map = state.get_map()
        block_config = state.get_config()
        next_config = []
        
        if action == Action.UP:
            next_config = Action.move_up(map, block_config)
        elif action == Action.DOWN:
            next_config = Action.move_down(map, block_config)
        elif action == Action.LEFT:
            next_config = Action.move_left(map, block_config)
        elif action == Action.RIGHT:
            next_config = Action.move_right(map, block_config)
        next_state = GameState(map, next_config)

        return next_state

    def move_up(map, block_config):
        """
        UPRIGHT: CHANGEW ROW - FIXED COLUMN: [(1,1),(2,3), 0]
        POINT_1 ALLWAY <= POINT_2
        """
        current_row_1 = block_config[0][0]
        current_column_1 = block_config[0][1]
        
        current_row_2 = block_config[1][0]
        current_column_2 = block_config[1][1]
        
        current_status = block_config[2]

        next_row_1 = -1
        next_row_2 = -1
        next_status = -1

        if current_status == 0:
            "UPRIGHT: ROW_1 = ROW_2 - COLUMN_1 = COLUMN_2"
            next_row_1 = current_row_1 - 2
            next_row_2 = current_row_2 - 1
            next_status = 1 # to vertical
        
        elif current_status == 1:
            "VERTICAL: ROW_1 # ROW_2 - COLUMN_1 = COLUMN_2"
            next_row_1 = current_row_1 - 1
            next_row_2 = current_row_2 - 2
            next_status = 0 # to upright
       
        elif current_status == 2:
            "HORIZONTAL: ROW_1 = ROW_2 - COLUMN_1 # COLUMN_2"
            next_row_1 = current_row_1 - 1
            next_row_2 = current_row_2 - 1
            next_status = 2 # nochange

        next_postion_1 = (next_row_1, current_column_1)
        next_postion_2 = (next_row_2, current_column_2)

        next_conf = [next_postion_1, next_postion_2, next_status]

        return next_conf

    def move_down(map, block_config):
        """
        UPRIGHT: CHANGEW ROW - FIXED COLUMN: [(1,1),(2,3), 0]
        POINT_1 ALLWAY <= POINT_2
        """
        current_row_1 = block_config[0][0]
        current_column_1 = block_config[0][1]
        
        current_row_2 = block_config[1][0]
        current_column_2 = block_config[1][1]
        
        current_status = block_config[2]

        next_row_1 = -1
        next_row_2 = -1
        next_status = -1

        if current_status == 0:
            "UPRIGHT: ROW_1 = ROW_2 - COLUMN_1 = COLUMN_2"
            next_row_1 = current_row_2 + 1
            next_row_2 = current_row_1 + 2
            next_status = 1
        
        elif current_status == 1:
            "VERTICAL: ROW_1 # ROW_2 - COLUMN_1 = COLUMN_2"
            next_row_1 = current_row_1 + 2
            next_row_2 = current_row_2 + 1
            next_status = 0
       
        elif current_status == 2:
            "HORIZONTAL: ROW_1 = ROW_2 - COLUMN_1 # COLUMN_2"
            next_row_1 = current_row_1 + 1
            next_row_2 = current_row_2 + 1
            next_status = 2

        next_postion_1 = (next_row_1, current_column_1)
        next_postion_2 = (next_row_2, current_column_2)

        next_conf = [next_postion_1, next_postion_2, next_status]
        return next_conf
    
    def move_left(map, block_config):
        """
        UPRIGHT: FIXED ROW - CHANGE COLUMN
        POINT_1 ALLWAY <= POINT_2
        """
        current_row_1 = block_config[0][0]
        current_column_1 = block_config[0][1]
        
        current_row_2 = block_config[1][0]
        current_column_2 = block_config[1][1]
        
        current_status = block_config[2]

        next_column_1 = -1
        next_column_2 = -1
        next_status = -1

        if current_status == 0:
            "UPRIGHT: ROW_1 = ROW_2 - COLUMN_1 = COLUMN_2"
            next_column_1 = current_column_1 - 2
            next_column_2 = current_column_2 - 1
            next_status = 2
        
        elif current_status == 1:
            "VERTICAL: ROW_1 # ROW_2 - COLUMN_1 = COLUMN_2"
            next_column_1 = current_column_1 - 1
            next_column_2 = current_column_2 - 1
            next_status = 1
       
        elif current_status == 2:
            "HORIZONTAL: ROW_1 = ROW_2 - COLUMN_1 # COLUMN_2"
            next_column_1 = current_column_1 - 1
            next_column_2 = current_column_2 - 2
            next_status = 0

        next_postion_1 = (current_row_1, next_column_1)
        next_postion_2 = (current_row_2, next_column_2)

        next_conf = [next_postion_1, next_postion_2, next_status]

        return next_conf

    def move_right(map, block_config):
        """
        UPRIGHT: FIXED ROW - CHANGE COLUMN
        POINT_1 ALLWAY <= POINT_2
        """
        current_row_1 = block_config[0][0]
        current_column_1 = block_config[0][1]
        
        current_row_2 = block_config[1][0]
        current_column_2 = block_config[1][1]
        
        current_status = block_config[2]

        next_column_1 = -1
        next_column_2 = -1
        next_status = -1

        if current_status == 0:
            "UPRIGHT: ROW_1 = ROW_2 - COLUMN_1 = COLUMN_2"
            next_column_1 = current_column_2 + 1
            next_column_2 = current_column_1 + 2
            next_status = 2
        
        elif current_status == 1:
            "VERTICAL: ROW_1 # ROW_2 - COLUMN_1 = COLUMN_2"
            next_column_1 = current_column_1 + 1
            next_column_2 = current_column_2 + 1
            next_status = 1
       
        elif current_status == 2:
            "HORIZONTAL: ROW_1 = ROW_2 - COLUMN_1 # COLUMN_2"
            next_column_1 = current_column_1 + 2
            next_column_2 = current_column_2 + 1
            next_status = 0

        next_postion_1 = (current_row_1, next_column_1)
        next_postion_2 = (current_row_2, next_column_2)

        next_conf = [next_postion_1, next_postion_2, next_status]
        return next_conf