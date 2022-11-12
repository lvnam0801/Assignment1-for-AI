from library.container import Stack, Queue, PriorityQueue, Visited
from typing import List


import library.container as container
import random
import config

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
        container.raise_no_defined()
    
    def is_goal_state(self, state):
        """
        Return True if and only the state is a valid goal state
        """
        container.raise_no_defined()
    
    def get_successor(self, state):
        """
        For a given state, this should ruturn a list of tripple(successor, action, stepCost), where successor is a successor to the current state, 'action' is the action requried to get there, and 'stepCost' is the incremental cost of expanding to that succussor.
        """
        container.raise_no_defined()
    
    def get_cost_of_action(self, action):
        """
        Actions: a list of actions to take
        This method retur total cost of a particular sequence of actions. The sequence must be composed of legal moves.
        """
        container.raise_no_defined()

def graph_search(problem, data_structure):
    """
    The algorithm return a actions list to move from start state to goal state.
    """
    start_state = problem.get_start_state()
    visited, fringe = Visited(), data_structure() 

    fringe.push((start_state, []))

    while not fringe.is_empty(): 
        state, path = fringe.pop()
        if(problem.is_goal_state(state)):
            return path

        if visited.check_in_visited(state) == False:
            next_states = problem.get_successor(state) 
            visited.add(state)
            for next in next_states:
                if visited.check_in_visited(next[0]) == False:
                    fringe.push((next[0], path + [next[1]]))
    return []

def a_start_search(problem, heuristic= lambda: 0):
    """
    Search the node that has the lowest of f(n): g(n) + h(n).
    """
    start_state = problem.get_start_state()
    visited, fringe = Visited(), PriorityQueue()
    fringe.push((start_state, [], 0), 0)
    
    while not fringe.is_empty(): 
        state, path, cost = fringe.pop()
        
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

class Population:
    """
    There is interface to implement the population.
    """
    class Individual:
        """
        The individual (type of population) in the population
        """
        def __init__(self, path, state_list) -> None:
            pass
        
        def pair(self, other: "Population.Individual") -> "Population.Individual":
            pass
        
        def __len__(self) -> int:
            pass
        
    def generate_population(problem, N = 2) -> List[Individual]:
        """
        The algorithm return a population of idividual.
        """
        pass

    def heuristic_bloxorz(individual: Individual):
        pass
    
    def sort_population(population: List[Individual]):
        pass

    def mutate(individual: Individual, problem) -> Individual:
        pass
    
    def peek_top(population: List[Individual], top=0):
        pass

def search_genertic(problem, populatioin: Population):
    
    MUTATE_RATE = config.MUTATE_RATE
    NUMBER_LOOP = config.NUMBER_LOOP
    POPULATION_SIZE = config.POPULATION_SIZE
    
    init_population = populatioin.generate_population(problem, POPULATION_SIZE)
    if len(init_population) == 0:
        return []
    
    old_population = init_population
    
    for _ in range(NUMBER_LOOP):
        
        new_population = []
        old_population = populatioin.sort_population(old_population)
        
        for i in range(len(old_population) - 1):
            parent_x = populatioin.peek_top(old_population, i)
            parent_y = populatioin.peek_top(old_population, i + 1)

            child = parent_x.pair(parent_y)
            if child != None:
                new_population.append(child)
                if random.randint(0, MUTATE_RATE) == 0:
                    child = populatioin.mutate(child, problem)
        if len(new_population) >= 1:
            old_population = new_population
    
    top = populatioin.peek_top(old_population)
    return top.path[1:]