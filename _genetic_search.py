from typing import Set
import random
import copy

class Individual:

    def __init__(self) -> None:
        pass

    def pair(self, other: "Individual") -> "Individual":
        pass

def heuristic_bloxorz():
    return None

def heuristic_select(population: Set[Individual], heuristic=heuristic_bloxorz) -> Individual:
    return None

def mutate(individual: Individual) -> Individual:
    return None

def peek_top(population: Set[Individual], num_top=1) -> Individual:
    return None

def generate_population(problem, N = 2):
    """
    The algorithm return a population of idividual.
    """
    start_state = problem.get_start_state()
    initial_tracer = (start_state, [0], [start_state.get_config()])
    current_tracer = copy.deepcopy(initial_tracer)
    solutions = set()

    while len(solutions) < N:
        try:
            state, path, config = current_tracer
            if(problem.is_goal_state(state)):
                solutions.add([path, config])
                current_tracer = copy.deepcopy(initial_tracer)
                continue
            next_states = problem.get_successor(state)
            index = random.randint(0, len(next_states) - 1)
            next = next_states[index]
            current_tracer = (next[0], path + [next[1]], config + [next[0].get_config()])
        except Exception as e:
            print(e, index, len(next_states))
    return solutions

def genertic_search(problem, data_structure):

    N = 2
    MUTATE_RATE = 100

    init_population: Set[data_structure] = generate_population(problem, data_structure)
    old_population = init_population

    for _ in range(N):
        new_population: Set[data_structure] = set()
        for _ in len(old_population):

            parent_x: data_structure = heuristic_select(old_population, heuristic_bloxorz)
            parent_y: data_structure = heuristic_select(old_population, heuristic_bloxorz)
            
            child: data_structure = parent_x.pair(parent_y)
            # if random.randint(0, MUTATE_RATE) == 0:
            #     child = mutate(child)
            new_population.add(child)
        old_population = new_population

    top: data_structure = peek_top(old_population)
    print(top)