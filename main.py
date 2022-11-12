import load_data as load_data 
import resource
import time
import agent
import sys

start_time = time.time()
start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


if __name__== "__main__":
    argv = sys.argv
    
    prevent = False
    if len(argv) < 4:
        print("Please run [option]:  python3 main.py [water-sort, bloxorz] [all-level, level-1, level-2,..] [dfs, bfs, a-start] [visualize]")
        print("Ex:     python3 main.py water-sort all-level a-start visualize")
        print()
    
    elif argv[1] not in ['water-sort', 'bloxorz']:
        print(argv[1])
        print("You must select the game: 'water-sort', 'bloxorz'")
        print("Ex:     python3 main.py water-sort all-level a-start visualize")
        print()
    
    elif argv[2] == 'all-level':
        for option in argv[3:]:
            if option not in ['dfs', 'bfs', 'a-start', 'genertic', 'visualize']:
                print("Option for search strategy: ['dfs', 'bfs', 'a-start', 'genertic']")
                print("Option visualize: ['visualize']")
            else:
                prevent = True
    else :
        if len(argv[2]) < 6 or argv[2][:6] != 'level-':
                print("Please set level correct format:")
                print("Ex: main.py water-sort level-1 a-start visualize")
        elif int(argv[2][6]) < 1 and int(argv[2][6] > 2):
            print("Level must be in [1-3]: Ex: level-1, level-2,...")
        else:
            for option in argv[3:]:
                if option not in ['dfs', 'bfs', 'a-start', 'genertic', 'visualize']:
                    print("Option for search strategy: ['dfs', 'bfs', 'a-start', 'genertic']")
                    print("Option visualize: ['visualize']")
                    break
            else:
                prevent = True


    if prevent == True:
        if argv[1] == 'water-sort':
            data_water_sort = load_data.load_data_water()
            if argv[2] == 'all-level':
                for idx in range(len(data_water_sort)):
                    print("------------------ LEVEL: {}---------------------".format(idx + 1))
                    agent.solve_water_sort(data_water_sort[idx], argv[3:])
            else:
                level = int(argv[2][6]) - 1
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

    



end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
end_time = time.time()

print("[TIME(s): {:.2f}]".format(end_time - start_time))
print("[MEMORY(mb): {:.2f}]".format((end_mem - start_mem)/1024))