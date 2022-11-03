import inspect


class Stack:

    """A container with a Last-In-First-Out (LIFO) queuing policy."""

    def __init__(self) -> None:
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


class Queue:
    """A container with a first-in-first-out (FIFO) queuing policy."""
    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.queue.insert(0, item)
    
    def pop(self):
        "Dequeue the 'item' in front of the queue (This operation will remove item from the queue)"
        return self.queue.pop()

    def is_empty(self):
        """Return True if queue is empty."""
        if len(self.list) == 0:
            return True


def raise_no_defined():
    file_name = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    
    print("Method not implemented: %s at line %s of %s"(method, line, file_name))