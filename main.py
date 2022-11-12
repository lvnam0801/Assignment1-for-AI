import time
import tracemalloc
import sys
import util

#---Measure resource---#
tracemalloc.start()
start_time = time.time()
#----------------------#

if __name__== "__main__":
    argv = sys.argv
    if util.check_argv(argv):
        util.seach(argv)
   
#---Measure resource---#
end_time = time.time()
tracemalloc.stop
mem = tracemalloc.get_traced_memory()
print("[TIME(s): {:.5f}]".format(end_time - start_time))
print("[MAX MEMORY(mb): {:.5f}]".format(mem[1]/(1024*1024)))
#----------------------#