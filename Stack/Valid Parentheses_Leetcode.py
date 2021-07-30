# https://leetcode.com/problems/valid-parentheses/
from collections import deque
class Solution:
    def isValid(self, s: str):
        self.stack = deque()
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c == '(' or c =='[' or c == '{':
                self.stack.append(c)
                continue

            if c == ')' and len(self.stack)>0 and self.stack[-1]=='(':
                self.stack.pop()
            elif c == '}' and len(self.stack) > 0 and self.stack[-1] == '{':
                self.stack.pop()
            elif c == ']' and len(self.stack) >0 and self.stack[-1] == '[':
                self.stack.pop()
            else:
                return False
        if len(self.stack)==0: return True
        else: return False


s = Solution()
print(s.isValid("(("))
