# https://www.youtube.com/watch?v=rYkfBRtMJr8&list=PLgUwDviBIf0rQ6cnlaHRMuOp4H_D-7hwP&index=4
# https://practice.geeksforgeeks.org/problems/subset-sums2234/1

class Solution:
    def subsetSums(self,arr,N):
        ind = sum = 0
        self.ans = []
        ans = self.subset(ind,sum,arr,self.ans[:])
        ans.sort()
        return ans

    def subset(self,ind,sum,arr,ans):
        if ind == len(arr):
            self.ans.append(sum)
            return
        else:
            # Pick
            sum += arr[ind]
            self.subset(ind+1,sum,arr,ans)
            #Non Pick
            sum -= arr[ind]
            self.subset(ind+1,sum,arr,ans)
        return self.ans

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        for x in ans:
            print(x,end=" ")
        print("")


'''
input
1
2
2 3
------
1
3
5 2 1
----
1
2
1 2 2
'''
