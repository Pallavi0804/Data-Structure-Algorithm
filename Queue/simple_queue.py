from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,value):
        self.queue.appendleft(value)

    def dequeue(self):
        self.queue.pop()

    def is_empty(self):
        if len(self.queue) == 0:return True

    def length(self):
        return len(self.queue)

    def printQueue(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=' ')


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.is_empty())
print(q.length())
q.printQueue()

