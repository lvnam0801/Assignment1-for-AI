import resource
import time

start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start_time = time.time()


end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
end_time = time.time()

print("MEMORY USED: ", (end_mem - start_mem)/1024, "MB")
print("TIME TO SEARCH: ", (end_time - start_time), "s")
    
