import heapq
import inspect

class Stack:
    """
    A container with a Last-In-First-Out (LIFO) queuing policy.
    """
    def __init__(self):
        self.list = []
    
    def push(self, item):
        "Push 'item' ontop stack"
        self.list.append(item)
    
    def pop(self):
        "Pop the item on-top of stack"
        return self.list.pop()
    
    def is_empty(self):
        if len(self.list) == 0: 
            return True

    def __len__(self):
        return len(self.list)

class Queue:
    """
    A container with a first-in-first-out (FIFO) queuing policy.
    """
    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)
    
    def pop(self):
        "Dequeue the 'item' in front of the queue (This operation will remove item from the queue)"
        return self.list.pop()

    def is_empty(self):
        """Return True if queue is empty."""
        if len(self.list) == 0:
            return True

class PriorityQueue:
    """
    Store element in heap with the priority to pop the element with highest priority
    """
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1
    
    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item
    
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
    
    def update_heap(self, item, priority):
        """
        If item already in heap with higher priority, do nothing
        If item already in heap with lower priority, delete it and rebuild heap, push new item
        If item not already in heap, simple is push it to heap
        """
        for index, (p, c, i) in enumerate(self.heap):
            if item[0].compare(i[0]) == True:
                if priority >= p: # heap: min-heap
                    return
                self.heap[index] = self.heap[-1]
                self.heap.pop()
                heapq.heapify(self.heap)
        self.push(item, priority)

class Visited:
    """
    Save all state was visited.
    """
    def __init__(self):
        self.visited = []

    def add(self, state):
        self.visited.append(state)
    
    def check_in_visited(self, state):
        for v_state in self.visited:
            if state.compare(v_state) == True:
                return True
        return False

def raise_no_defined():
    file_name = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    print("Method not implemented: %s at line %s of %s".format(method, line, file_name))