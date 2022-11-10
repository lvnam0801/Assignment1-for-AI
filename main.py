from problem import WaterProblem, BloxorzProblem
from search import search_BFS, search_DFS, search_informed, graph_travel
import data
from library import Stack, Queue

# import resource
# import time

if __name__== "__main__":
    
    # start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # start_time = time.time()

    # -------------------------- Water Sort ---------------------#
    # water_problem = WaterProblem(data.water_config_1)
    # path_1 = search_DFS(water_problem)
    # path_2 = search_BFS(water_problem)
    # path_3 = search_informed(water_problem)

    # water_problem = WaterProblem(data.water_config_2)
    # path_1 = search_DFS(water_problem)
    # path_2 = search_BFS(water_problem)
    # path_3 = search_informed(water_problem)

    # print("DFS SEARCH: ", path_1)
    # print("BFS SEARCH: ", path_2)
    # print("A_S SEARCH: ", path_3)

    # -------------------------- Bloxorz ---------------------#
    bloxorz_problem = BloxorzProblem(data.bloxorz_config_1)
    paths = graph_travel(bloxorz_problem, Stack, 10)
    print(len(paths))
    for path in paths:
        print(path[:10], len(path))
    
    # end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # end_time = time.time()

    # print("MEMORY USED: ", (end_mem - start_mem)/1024, "MB")
    # print("TIME TO SEARCH: ", (end_time - start_time), "s")
    
