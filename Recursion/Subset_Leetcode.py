#https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums):
        ind = 0
        arr = nums[:]
        ds = self.ans = []
        return self.findsubset(ind,arr[:],ds[:],self.ans[:])

    def findsubset(self,ind,arr,ds,ans):
        if ds not in self.ans:
            self.ans.append(ds[:])
        if ind == len(arr):
            return
        for i in range(ind,len(arr)):
           # if i!=ind and arr[i] == arr[i-1]:
                #continue
            ds.append(arr[i])
            self.findsubset(i+1,arr[:],ds[:],self.ans[:])
            ds.pop()
        return self.ans[:]

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ans = ob.subsetsWithDup(arr)
    print(ans)
