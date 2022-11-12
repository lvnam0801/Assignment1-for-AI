import load_data
import agent
import tracemalloc

def check_argv(argv: list):
    if len(argv) < 4:
        print("Please run:")
        print("          python3 main.py [water-sort, bloxorz] [all-level, level-1, level-2,..] [dfs, bfs, a-start] [visualize]")
        print("Ex:")
        print("          python3 main.py water-sort all-level a-start visualize")
        print("          python3 main.py bloxorz all-level genertic visualize")
        print()
    
    elif argv[1] not in ['water-sort', 'bloxorz']:
        print(argv[1])
        print("You must select the game: 'water-sort', 'bloxorz'")
        print("Ex:")
        print("          python3 main.py water-sort all-level a-start visualize")
        print()
    
    elif argv[2] == 'all-level':
        for option in argv[3:]:
            if option not in ['dfs', 'bfs', 'a-start', 'genertic', 'visualize']:
                print("Option for search strategy: ['dfs', 'bfs', 'a-start', 'genertic']")
                print("Option visualize: ['visualize']")
            else:
                return True
    else :
        if len(argv[2]) < 6 or argv[2][:6] != 'level-':
            print("Please set level correct format:")
            print("Ex:\n          main.py water-sort level-1 a-start visualize")
        elif int(argv[2][6]) < 1:
            print("Level must be in [1-3]: Ex: level-1, level-2,...")
        else:
            for option in argv[3:]:
                if option not in ['dfs', 'bfs', 'a-start', 'genertic', 'visualize']:
                    print("Option for search strategy: ['dfs', 'bfs', 'a-start', 'genertic']")
                    print("Option visualize: ['visualize']")
                    break
            else:
                return True

def seach(argv: list):
    try:
        if argv[1] == 'water-sort':
            data_water_sort = load_data.load_data_water()
            if argv[2] == 'all-level':
                for idx in range(len(data_water_sort)):
                    print("------------------ LEVEL: {}---------------------".format(idx + 1))
                    agent.solve_water_sort(data_water_sort[idx], argv[3:])
            else:
                level = int(argv[2][6:]) - 1
                print("------------------ LEVEL: {}---------------------".format(level + 1))
                agent.solve_water_sort(data_water_sort[level], argv[3:])

        elif argv[1] == 'bloxorz':
            data_bloxorz = load_data.load_data_bloxorz()
            if argv[2] == 'all-level':
                for idx in range(len(data_bloxorz)):
                    print("------------------ LEVEL: {}---------------------".format(idx))
                    agent.solve_bloxorz(data_bloxorz[idx], argv[3:])
            else:
                level = int(argv[2][6]) - 1
                print("------------------ LEVEL: {}---------------------".format(level + 1))
                agent.solve_bloxorz(data_bloxorz[level], argv[3:])
    except Exception as E:
        print("Maybe level out of rank: {}".format(E))