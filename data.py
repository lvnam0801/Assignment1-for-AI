
# --------------------- WATER SORT --------------------#
tube1 = ['Y', 'B', 'R', 'B']
tube2 = ['B', 'Y', 'R', 'B']
tube3 = ['R', 'B', 'Y', 'R']
tube4 = []
tube5 = []

data_0 = [tube1, tube2, tube3, tube4, tube5]
#
tube1 = ['Y', 'B', 'R', 'Y']
tube2 = ['B', 'R', 'Y', 'Y']
tube3 = ['B', 'R', 'B', 'R']
tube4 = []
tube5 = []

data_1 = [tube1, tube2, tube3, tube4, tube5]

# ------------------------ BLOXORZ --------------------#
map = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 5, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]
start_position = [(1 , 1), (1 , 1), 0]
goal_position = [(4, 7),(4, 7), 0]

data_2 = [map, start_position, goal_position]