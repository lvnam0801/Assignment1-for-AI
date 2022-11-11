from game.problem import WaterProblem, BloxorzProblem
import game.data as data
from search import search_BFS, search_DFS, search_informed


def water_test():
    #------------------------- Water Sort ---------------------#
    water_problem = WaterProblem(data.water_config_1)
    path_1 = search_DFS(water_problem)
    path_2 = search_BFS(water_problem)
    path_3 = search_informed(water_problem)

    water_problem = WaterProblem(data.water_config_2)
    path_1 = search_DFS(water_problem)
    path_2 = search_BFS(water_problem)
    path_3 = search_informed(water_problem)

    print("DFS SEARCH: ", path_1)
    print("BFS SEARCH: ", path_2)
    print("A_S SEARCH: ", path_3)

def bloxorz_test():

    # -------------------------- Bloxorz ---------------------#
    # bloxorz_problem = BloxorzProblem(data.bloxorz_config_1)
    # paths = graph_travel(bloxorz_problem, Stack, 10)
    # print(len(paths))
    # for path in paths:
    #     print(path[:10], len(path))
    pass