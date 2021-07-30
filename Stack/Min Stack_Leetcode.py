# https://leetcode.com/problems/min-stack/
from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        """
        initialize your data structure here.
        """
    def push(self, val: int):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        min = self.stack[0]
        for i in range(1,len(self.stack)):
            #print(self.stack[i],self.stack[i-1])
            if self.stack[i] < min:
                min = self.stack[i]
        return min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-1))
print(obj.getMin())
print(obj.top())
print(obj.pop())
print(obj.getMin())
