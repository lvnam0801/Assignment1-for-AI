from problem import WaterProblem
from water_sort import heuristic
from search import search_BFS, search_DFS, search_informed


tube1 = ['Y', 'Y', 'R', 'B']
tube2 = ['B', 'Y', 'R', 'B']
tube3 = ['R', 'B', 'Y', 'R']
tube4 = []
tube5 = []

data = [tube1, tube2, tube3, tube4, tube5]


if __name__== "__main__":
    problem = WaterProblem(data)

    path_1 = search_DFS(problem)
    path_2 = search_BFS(problem)
    path_3 = search_informed(problem, heuristic)

    print("DFS SEARCH: ", path_1)
    print("BFS SEARCH: ", path_2)
    print("A_S SEARCH: ", path_3)
