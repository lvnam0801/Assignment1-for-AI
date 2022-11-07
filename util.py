import inspect

def raise_no_defined():
    file_name = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    print("Method not implemented: %s at line %s of %s".format(method, line, file_name))

def print_config(config):
    for tube in config:
        print(tube.list)