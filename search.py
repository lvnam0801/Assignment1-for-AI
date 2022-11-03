import util
from util import Stack, Queue

class SearchProblem:
    
    """
    This class outlines the structure of a search problem.
    """
    
    def get_start_state(self):
        """
        Return start state for the search problems
        """
        util.raise_no_defined()
    
    def is_goal_state(self, state):
        """
        Return True if and only the state is a valid goal state
        """
        util.raise_no_defined()
    
    def get_successor(self, state):
        """
        For a given state, this should ruturn a list of tripple(successor, action, stepCost), where successor is a successor to the current state, 'action' is the action requried to get there, and 'stepCost' is the incremental cost of expanding to that succussor.
        """
        util.raise_no_defined()
    
    def get_cost_of_action(self, actions):
        """
        Actions: a list of actions to take
        This method retur total cost of a particular sequence of actions. The sequence must be composed of legal moves.
        """
        util.raise_no_defined()



def graph_search(problem, data_structure):
    """
    The algorithm return a actions list to move from start state to goal state.
    """
    start_state = problem.get_start_state()
    visited, fringe = set(), data_structure()

    "Fringe contain the current state and path (actions sequence) to move to current state"
    fringe.push((start_state, [])) 

    while not fringe.is_empty():
        state, path = fringe.pop()

        if(problem.is_goal_state(state)):
            return path
        
        if state not in visited:
            
            next_states = problem.get_successor(state)
            visited.add(state)

            for next in next_states:
                if(next[0] not in visited):
                    fringe.push((next[0]), path + [[next[1]]])
    return []

def search_DFS(problem):
    """
    Search tree with DFS (search first deepest node in the tree)
    """
    return graph_search(problem, Stack)

def search_BFS(problem):
    """
    Search the first shallowest node in the tree search
    """
    return graph_search(problem, Queue)