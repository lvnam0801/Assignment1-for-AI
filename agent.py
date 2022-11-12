import config.problem as problem
import config.visualize as visualize
import library.search as search

def solve_water_sort(data_config_game, argv):
    """
    Agent to find a path to goal state.
    """
    water_problem = problem.WaterProblem(data_config_game)
    path = []
    if 'dfs' in argv:
        print("\nWATER SORT: Search DFS....")
        path = search.search_DFS(water_problem)
        print("\nSOLUTION: ", path)
        print()
    if 'bfs' in argv:
        print("\nWATER SORT: Search BFS....")
        path = search.search_BFS(water_problem)
        print("\nSOLUTION: ", path)
        print()
    if 'a-start' in argv:
        print("\nWATER SORT: Search A*....")
        path = search.search_informed(water_problem)
        print("\nSOLUTION: ", path)
        print()
    if 'visualize' in argv:
        print("VISUALIZE")
        visualize.visualize_water_sort(water_problem, path)
    

def solve_bloxorz(data_config_game: list, search_strategy: list):
    """
    Agent to find a path to goal state.
    """
    bloxorz_problem = problem.BloxorzProblem(data_config_game)
    path = []

    if 'dfs' in search_strategy:
        print("BLOXORZ: Search DFS................")
        path = search.search_DFS(bloxorz_problem)
        print("PATH: ", path)

    if 'bfs' in search_strategy:
        print()
        print("BLOXORZ: Search BFS................")
        path = search.search_BFS(bloxorz_problem)
        print("PATH: ", path)
        print()
    if 'genertic' in search_strategy:
        path = search.search_genertic(bloxorz_problem, problem.BloxorzPopulation)
        print("PATH: ", path)
        print()
    if 'visualize' in search_strategy:
        visualize.visualize_bloxorz(bloxorz_problem, path)


