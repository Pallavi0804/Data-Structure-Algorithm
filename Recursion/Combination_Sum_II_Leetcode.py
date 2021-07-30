# https://leetcode.com/problems/combination-sum-ii/
import sys
sys.setrecursionlimit(10**6)
import ast
class Solution:
    def combinationSum2(self, candidates, target):
        ind = sum = 0
        ds = []
        self.ans =[]
        final_res = []
        s = self.findCombination(ind,candidates,target,sum,ds[:],self.ans[:])
        for i in s:
            final_res.append(ast.literal_eval(i))
        return final_res

    def findCombination(self,ind,candidates,target,sum,ds,ans):
        if sum == target:
            self.ans.append(ds[:])
        if ind == len(candidates):
            return
        for i in range(ind,len(candidates)):
            if sum < target:
                sum += candidates[i]
                ds.append(candidates[i])
                self.findCombination(i+1,candidates,target,sum,ds[:],self.ans[:])
                sum -= candidates[i]
                ds.pop()
        for i in range(len(self.ans)):
            self.ans[i].sort()
        s = set(str(x) for x in self.ans)
        return s


if __name__ == '__main__':
    target = int(input())
    candidate = [int(x) for x in input().split()]
    ob = Solution()
    print(ob.combinationSum2(candidate,target))
