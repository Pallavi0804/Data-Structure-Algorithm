from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
        return self.length()==0

    def length(self):
        return len(self.container)

    def display(self):
        for i in range(self.length()):
            print(self.container[i],end=' ')
        print("\n")


s = Stack()
s.push(50)
s.push(40)
s.push(30)
s.push(20)
s.push(10)
s.display()
s.pop()
s.display()
