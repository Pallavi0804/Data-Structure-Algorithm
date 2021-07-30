# https://leetcode.com/problems/subsets-ii/
# https://www.youtube.com/watch?v=RIn3gOkbhQE&list=PLgUwDviBIf0rQ6cnlaHRMuOp4H_D-7hwP&index=5

# Not Completed yet - Incomplete code
class Solution():
    def subsetsWithDup(self, nums):
        self.nums = nums
        self.ds = []
        self.ind = 0
        self.ans = []
        self.ans = self.subset(self.ind,self.ds,self.nums,self.ans)
        return self.ans

    def subset(self,ind,ds,nums,ans):
        if ind == len(nums):
            print(ds)
            self.ans.append(ds)
            return
        else:
            # Pick
            ds.append(nums[ind])
            self.subset(ind+1,ds,nums,self.ans)
            # Non Pick
            ds.pop()
            self.subset(ind+1,ds,nums,self.ans)
        return self.ans

nums = [1,2,2]
s = Solution()
print(s.subsetsWithDup(nums))
