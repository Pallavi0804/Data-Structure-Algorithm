# https://leetcode.com/problems/permutations/
# https://www.youtube.com/watch?v=YK78FU5Ffjw&list=PLgUwDviBIf0rQ6cnlaHRMuOp4H_D-7hwP&index=7

class Solution(object):
    def permute(self, nums):
        self.nums = nums
        self.ans = []
        self.map = [False] * len(nums)
        self.ds = []
        return self.calculate_per(self.nums,self.ans[:],self.map,self.ds[:])

    def calculate_per(self,nums,ans,map,ds):
        if len(ds) == len(nums):
            self.ans.append(ds)
            return
        for i in range(len(nums)):
            if map[i] == False:
                map[i] = True
                ds.append(nums[i])
                self.calculate_per(nums[:],self.ans[:],map[:],ds[:])
                ds.pop()
                map[i] = False
        return self.ans

nums = [1,2,3]
s = Solution()
print(s.permute(nums))
