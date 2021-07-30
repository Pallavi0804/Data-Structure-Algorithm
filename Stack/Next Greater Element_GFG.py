# Incomplete
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
from collections import deque
class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr, n):
        greater_array = []
        self.stack = deque()
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i]:
                if len(self.stack)==0:greater_array.append(arr[i+1])
            else: if self.stack[-1]:pass
            else:
                self.stack.append(i+1)

arr = [1,3,2,4]
n = 4
s = Solution()
s.nextLargerElement(arr,n)


