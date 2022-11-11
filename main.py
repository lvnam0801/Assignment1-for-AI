from game.problem import BloxorzProblem, BloxorzPopulation
from library.search import search_genertic
import data as data
import resource
import time


if __name__== "__main__":
    # -------------------------- Bloxorz ---------------------#
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()

    for i in range(1000):
        bloxorz_problem = BloxorzProblem(data.bloxorz_config_1)
        path = search_genertic(bloxorz_problem, BloxorzPopulation)
        print(len(path), path)

        end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        end_time = time.time()

        print("MEMORY USED: ", (end_mem - start_mem)/1024, "MB")
        print("TIME TO SEARCH: ", (end_time - start_time), "s")
        start_time = end_time
        start_mem = end_mem
    
