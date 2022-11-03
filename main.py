from water_conf import *
tube1 = ['blue', 'red', 'yellow', 'yellow']
tube2 = ['blue', 'red', 'yellow', 'blue']
tube3 = ['red', 'yellow', 'blue', 'red']
tube4 = ['blue']
tube5 = []

# First state for program
data = [tube1, tube2, tube3, tube4, tube5]

state = GameState(data)
state.print_configuration()
print("Possible actions:")
action_list = state.get_legal_actions()
print(action_list)

print("Take actions")
conf = Actions.pour_water(state, action_list[0])
print(action_list[0])
print_configuration(conf)