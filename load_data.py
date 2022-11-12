
import json



def load_data_bloxorz():
    input_file = open('./data/data_bloxorz.json')
    input_data = json.load(input_file)
    data = []
    for input in input_data:
        map = input['maps']
        start_position = [tuple(input['start']), tuple(input['start']), 0]
        end_position = [tuple(input['end']), tuple(input['end']), 0]
        data.append([map, start_position, end_position])
    return data


def load_data_water():
    input_file = open('./data/data_water.json')
    input_data = json.load(input_file)
    data = []
    for input in input_data:
        config = []
        for idx in range(len(input)):
            config.append(input["tube" + str(idx + 1)])
        data.append(config)
    return data