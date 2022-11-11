def mutate(individual: BloxorzIndividual, problem) -> BloxorzIndividual:
    # start_idx = random.randint(0, len(individual) - 3)
    # end_idx = random.randint(start_idx + 1, len(individual) - 1)


    # start_state = individual[start_idx]
    # end_state = individual[end_idx]

    # initial_tracer = (start_state, ['0'], [start_state])
    # current_tracer = copy.deepcopy(initial_tracer)
    
    # new_path = []

    # while True:
    #     state, path, state_list = current_tracer
    #     if state.get_config() == end_state.get_config():
    #         # make new individual
    #         return

    #     next_states = problem.get_successor(state)
    #     index = random.randint(0, len(next_states) - 1)
    #     next = next_states[index]
    #     current_tracer = (next[0], path + [next[1]], state_list + [next[0]])
    pass