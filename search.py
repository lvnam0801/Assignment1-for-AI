from library import Stack, Queue, PriorityQueue, Visited
import library
import random
import copy

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

def search_informed(problem):
    """
    Search the the first node with the least total cost first
    """
    return a_start_search(problem, problem.heuristic)

class SearchProblem:
    
    """
    This class outlines the structure of a search problem.
    """
    
    def get_start_state(self):
        """
        Return start state for the search problems
        """
        library.raise_no_defined()
    
    def is_goal_state(self, state):
        """
        Return True if and only the state is a valid goal state
        """
        library.raise_no_defined()
    
    def get_successor(self, state):
        """
        For a given state, this should ruturn a list of tripple(successor, action, stepCost), where successor is a successor to the current state, 'action' is the action requried to get there, and 'stepCost' is the incremental cost of expanding to that succussor.
        """
        library.raise_no_defined()
    
    def get_cost_of_action(self, action):
        """
        Actions: a list of actions to take
        This method retur total cost of a particular sequence of actions. The sequence must be composed of legal moves.
        """
        library.raise_no_defined()

def graph_travel(problem, data_structure, N = 2):
    """
    The algorithm return a actions list to move from start state to goal state.
    """
    start_state = problem.get_start_state()
    initial_tracer = (start_state, [])
    current_tracer = copy.deepcopy(initial_tracer)
    solutions = []

    while len(solutions) < N:
        try:
            state, path = current_tracer

            if(problem.is_goal_state(state)):
                solutions.append(path)
                current_tracer = copy.deepcopy(initial_tracer)
                continue
        
            next_states = problem.get_successor(state)
            index = random.randint(0, len(next_states) - 1)
            next = next_states[index]
            current_tracer = (next[0], path + [next[1]])
        except Exception as e:
            print(e, index, len(next_states))
    return solutions

def graph_search(problem, data_structure):
    """
    The algorithm return a actions list to move from start state to goal state.
    """
    start_state = problem.get_start_state()
    visited, fringe = Visited(), data_structure() 

    fringe.push((start_state, []))

    while not fringe.is_empty(): 
        state, path = fringe.pop()

        print('-----------------------------')
        state.print_state()
        print()

        if(problem.is_goal_state(state)):
            return path

        if visited.check_in_visited(state) == False:
            next_states = problem.get_successor(state) 
            visited.add(state)
            for next in next_states:
                if visited.check_in_visited(next[0]) == False:
                    fringe.push((next[0], path + [next[1]]))
    return []

def null_heuristic(state=None, problem=None):
    """This heuristic is trivial"""
    return 0

def a_start_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest of f(n): g(n) + h(n).
    """
    start_state = problem.get_start_state()
    visited, fringe = Visited(), PriorityQueue()
    fringe.push((start_state, [], 0), 0)
    
    while not fringe.is_empty(): 
        state, path, cost = fringe.pop()
        
        print('-----------------------------')
        state.print_state()
        print()

        if(problem.is_goal_state(state)):
            return path
        
        if visited.check_in_visited(state) == False: 
            
            next_states = problem.get_successor(state)
            visited.add(state)

            for next in next_states:
                if visited.check_in_visited(next[0]) == False:
                    g_cost = cost + next[2]
                    h_cost = problem.heuristic(next[0])
                    estimate_cost = g_cost + h_cost
                    fringe.update_heap((next[0], path + [next[1]], g_cost), estimate_cost)
    return []