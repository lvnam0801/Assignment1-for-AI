from typing import Set
import random

class Individual:

    def __init__(self) -> None:
        pass

    def pair(self, other: "Individual") -> "Individual":
        pass

def heuristic_select(population: Set[Individual], heuristic: function) -> Individual:
    return None

def heuristic_bloxorz():
    return None

def mutate(individual: Individual) -> Individual:
    return None

def peek_top(population: Set[Individual], num_top=1) -> Individual:
    return None

if __name__ == "__main__":
    N = 10
    MUTATE_RATE = 100
    init_population: Set[Individual] = set()
    old_population = init_population
    for _ in range(N):
        new_population: Set[Individual] = set()
        for _ in len(old_population):
            parent_x: Individual = heuristic_select(old_population, heuristic_bloxorz)
            parent_y: Individual = heuristic_select(old_population, heuristic_bloxorz)
            child: Individual = parent_x.pair(parent_y)
            if random.randint(0, MUTATE_RATE) == 0:
                child = mutate(child)
            new_population.add(child)
        old_population = new_population

    top: Individual = peek_top(old_population)
    print(top)