from water_sort import *
from agents import SearchAgent
from search import search_BFS, search_DFS

def set_data():
    tube1 = ['B', 'Y', 'B', 'Y']
    tube2 = ['Y', 'B', 'Y', 'B']
    tube3 = []

    # First state for program
    data = [tube1, tube2, tube3]
    return data

if __name__== "__main__":
    data = set_data()
    start_state = GameState(data)
    agent = SearchAgent(start_state)
    search_BFS(agent)


# def test(data):
#     root = GameState(data)
#     print("Root config")
#     print_config(root.get_config())
#     print()
#     print("Possible actions:")
#     action_list = root.get_legal_actions()
#     print(action_list)

#     print()
#     print("Take actions", action_list[0], sep=" ")
#     next_state = Actions.pour_water(root, action_list[0])
#     print_config(next_state.get_config())

#     print()
#     print("Print of root:")
#     print_config(root.get_config())