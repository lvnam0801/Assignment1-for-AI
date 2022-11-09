from problem import WaterProblem, BloxorzProblem
from search import search_BFS, search_DFS, search_informed
import data

if __name__== "__main__":
    
    # -------------------------- Water Sort ---------------------#
    # problem = WaterProblem(data.data_1)
    # path_3 = search_informed(problem)

    # path_1 = search_DFS(problem)
    # path_2 = search_BFS(problem)

    # print("DFS SEARCH: ", path_1)
    # print("BFS SEARCH: ", path_2)
    # print("A_S SEARCH: ", path_3)

    # -------------------------- Bloxorz ---------------------#
    problem = BloxorzProblem(data.data_2)
    path_1 = search_DFS(problem)
    path_2 = search_BFS(problem)

    print("DFS SEARCH: ", path_1)
    print("BFS SEARCH: ", path_2)
