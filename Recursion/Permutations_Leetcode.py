#https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        arr=nums
        ds = self.ans=[]
        return self.findPermutation(arr,ds[:],self.ans[:])

    def findPermutation(self,arr,ds,ans):
        if len(ds)==len(arr):
            self.ans.append(ds)
            return
        for i in range(len(arr)):
            if arr[i] not in ds:
                ds.append(arr[i])
                self.findPermutation(arr[:],ds[:],self.ans[:])
                ds.pop()
        return self.ans

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    ob = Solution()
    print(ob.permute(arr))
    #print(ans)
