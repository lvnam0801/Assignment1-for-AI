import copy
import random
from typing import List
import _genetic_search as search

class BloxorzIndividual(search.Individual):
    
    def __init__(self, path, state_list) -> None:
        self.path = path
        self.state_list = state_list

    def pair(self, other: "BloxorzIndividual") -> "BloxorzIndividual":

        SEGMENT_SIZE = 7

        segment = len(self)//SEGMENT_SIZE
        windowns_size = segment

        while windowns_size <= len(self)//2:
            for idx_1 in range(1, windowns_size):
                for idx_2 in range(-2,-windowns_size, -1):
                    if(self.state_list[idx_1].get_config() == other.state_list[idx_2].get_config()):
                        child = BloxorzIndividual(self.path[:idx_1 + 1] + other.path[idx_2 + 1:], self.state_list[:idx_1] + other.state_list[idx_2:])
                        return child
            windowns_size = windowns_size + segment
        
        return None

    def __len__(self):
        return len(self.state_list)

def generate_population(problem, data_structure=BloxorzIndividual, N = 2) -> List[BloxorzIndividual]:
    """
    The algorithm return a population of idividual.
    """
    start_state = problem.get_start_state()
    initial_tracer = (start_state, ['0'], [start_state])
    current_tracer = copy.deepcopy(initial_tracer)
    population = []

    while len(population) < N:
        state, path, config = current_tracer
        
        if(problem.is_goal_state(state)):
            population.append(data_structure(path, config))
            current_tracer = copy.deepcopy(initial_tracer)
            continue
        
        next_states = problem.get_successor(state)
        index = random.randint(0, len(next_states) - 1)
        next = next_states[index]
        current_tracer = (next[0], path + [next[1]], config + [next[0]])

    return population

def heuristic_bloxorz(individual: BloxorzIndividual):
    return len(individual)

def sort_population(population: List[BloxorzIndividual], heuristic=heuristic_bloxorz):
    new_population = sorted(population, key = lambda x: heuristic_bloxorz(x))
    return new_population

def mutate(individual: BloxorzIndividual, problem) -> BloxorzIndividual:
    start_idx = random.randint(0, len(individual) - 3)
    end_idx = random.randint(start_idx + 1, len(individual) - 1)


    start_state = individual.state_list[start_idx]
    end_state = individual.state_list[end_idx]

    initial_tracer = (start_state, ['0'], [start_state])
    current_tracer = copy.deepcopy(initial_tracer)
    
    while True:
        state, path, state_list = current_tracer
        if state.get_config() == end_state.get_config():
            new_path = individual.path[:start_idx + 1] + path[1:] + individual.path[end_idx + 1:]
            new_state_list = individual.state_list[:start_idx + 1] + state_list[1:] + individual.state_list[end_idx + 1:]
            new_individual = BloxorzIndividual(new_path, new_state_list)
            return new_individual

        next_states = problem.get_successor(state)
        index = random.randint(0, len(next_states) - 1)
        next = next_states[index]
        current_tracer = (next[0], path + [next[1]], state_list + [next[0]])

def peek_top(population: List[BloxorzIndividual], top=0):
    return population[top]

def genertic_search(problem, data_structure = BloxorzIndividual):
    
    N = 100
    MUTATE_RATE = 100
    
    init_population: List[data_structure] = generate_population(problem, data_structure, 100)
    old_population = init_population
    
    for _ in range(N):
        
        new_population: List[data_structure] = []
        old_population = sort_population(old_population)
        
        for i in range(len(old_population) - 1):
            parent_x: data_structure = peek_top(old_population, i)
            parent_y: data_structure = peek_top(old_population, i + 1)

            child: data_structure = parent_x.pair(parent_y)
            if child != None:
                new_population.append(child)
                if random.randint(0, MUTATE_RATE) == 0:
                    child = mutate(child, problem)
        if len(new_population) >= 1:
            old_population = new_population
    
    top: data_structure = peek_top(old_population)
    return top.path


