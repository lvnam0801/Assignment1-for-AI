from typing import Set
from game.problem import BloxorzProblem
from bloxorz_problem import genertic_search
import game.data as data


if __name__== "__main__":
    # -------------------------- Bloxorz ---------------------#
    bloxorz_problem = BloxorzProblem(data.bloxorz_config_1)
    path = genertic_search(bloxorz_problem)
    print(len(path), path)
    
