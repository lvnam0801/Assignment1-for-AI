import game.water_sort as water_sort
import game.bloxorz as bloxorz
import library.search as search
from typing import List
import copy
import random

class WaterProblem(search.SearchProblem):
    """
    Agents to search goal state of Water Color
    """
    
    def __init__(self, data):
        self.game_state = water_sort.GameState(data)

    def get_start_state(self):
        return self.game_state
    
    def is_goal_state(self, state):
        for tube in state.get_config():
            if tube.get_num_of_mixed() > 1:
                return False
            if len(tube.list) > 0 and len(tube.list) < water_sort.SIZE:
                return False
        return True

    def get_successor(self, state):
        successor = []
        possible_action_list = state.get_legal_actions()
        for action in possible_action_list: 
            next_state = water_sort.Actions.pour_water(state, action)
            cost = self.get_cost_of_action(action)
            successor.insert(0, [next_state, action, cost])
        return successor

    def get_cost_of_action(self, action):
        return 1     
    
    def heuristic(self, state):
        h_cost = state.get_all_mixed_count() - state.get_goal_mixed_count()
        return h_cost
   
class BloxorzProblem(search.SearchProblem):
    """
    Implement interface problem for BLOXORZ problem
    """
    def __init__(self, data):
        self.game_state = bloxorz.GameState(data[0], data[1])
        self.goal_state = bloxorz.GameState(data[0], data[2])
        self.get_successor(self.goal_state)

    def get_start_state(self):
        return self.game_state
    
    def is_goal_state(self, state):
        if(state.get_config() == self.goal_state.get_config()):
            return True
        return False

    def get_successor(self, state):
        successor = []
        action_list = state.get_legal_actions()
        for action in action_list:
            next_state = bloxorz.Action.move(state, action)
            cost = self.get_cost_of_action(action)
            successor.insert(0, [next_state, action, cost])

        return successor

    def get_cost_of_action(self, action):
        """
        Actions: a list of actions to take
        This method retur total cost of a particular sequence of actions. The sequence must be composed of legal moves.
        """
        return 1
    
class BloxorzPopulation(search.Population):
    """
    Population config for genertic search.
    """
    class Individual:
        def __init__(self, path, state_list) -> None:
            self.path = path
            self.state_list = state_list

        def pair(self, other: "BloxorzPopulation.Individual") -> "BloxorzPopulation.Individual":

            SEGMENT_SIZE = 7
            if self.find_match_position(other, SEGMENT_SIZE) != None:
                idx_1, idx_2 = self.find_match_position(other, SEGMENT_SIZE)
                child = BloxorzPopulation.Individual(self.path[:idx_1 + 1] + other.path[idx_2 + 1:], self.state_list[:idx_1] + other.state_list[idx_2:])
                return child
            return None
        
        def find_match_position(self, other, SEGMENT_SIZE=7):
            segment = len(self)//SEGMENT_SIZE
            windowns_size = segment

            while windowns_size <= len(self)//2:
                for idx_1 in range(1, windowns_size):
                    for idx_2 in range(-2,-windowns_size, -1):
                        if(self.state_list[idx_1].get_config() == other.state_list[idx_2].get_config()):
                            return [idx_1, idx_2]
                windowns_size = windowns_size + segment
            return None

        def __len__(self):
            return len(self.state_list)

    def generate_population(problem, N = 2) -> List[Individual]:
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
                population.append(BloxorzPopulation.Individual(path, config))
                current_tracer = copy.deepcopy(initial_tracer)
                continue
            
            next_states = problem.get_successor(state)
            index = random.randint(0, len(next_states) - 1)
            next = next_states[index]
            current_tracer = (next[0], path + [next[1]], config + [next[0]])
            
            "Prevent: no solution for the problem"
            if len(path) > 10000:
                break
        
        return population

    def heuristic_bloxorz(individual: Individual):
        return len(individual)

    def sort_population(population: List[Individual]):
        new_population = sorted(population, key = lambda x: BloxorzPopulation.heuristic_bloxorz(x))
        return new_population

    def mutate(individual: Individual, problem) -> Individual:
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
                new_individual = BloxorzPopulation.Individual(new_path, new_state_list)
                return new_individual

            next_states = problem.get_successor(state)
            index = random.randint(0, len(next_states) - 1)
            next = next_states[index]
            current_tracer = (next[0], path + [next[1]], state_list + [next[0]])

    def peek_top(population: List[Individual], top=0):
        return population[top]