import config.problem as problem
import config.water_sort as water_sort
import config.bloxorz as bloxorz

def visualize_water_sort(problem: problem.WaterProblem, path):
    """
    Visualize the progress to reach the goal state
    """
    start_state: water_sort.GameState = problem.get_start_state()
    current_state: water_sort.GameState = start_state
    
    print("-------")
    current_state.print_state()
    print()
    
    for action in path:
        current_state: water_sort.GameState =  water_sort.Actions.pour_water(current_state, action)
        print("-------")
        current_state.print_state()
        print()

def visualize_bloxorz(problem: problem.BloxorzProblem, path):
    """
    Visualize the progress to reach the goal state
    """
    start_state: bloxorz.GameState = problem.get_start_state()
    current_state: bloxorz.GameState = start_state
    
    print("--------")
    current_state.print_state()
    print()
    
    for action in path:
        current_state: bloxorz.GameState =  bloxorz.Action.move(current_state, action)
        print("-------")
        current_state.print_state()
        print()