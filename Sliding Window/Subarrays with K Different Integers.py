# https://leetcode.com/problems/subarrays-with-k-different-integers/
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A, K):
        distinct = defaultdict(int)
        i, kstart, total = 0, 0, 0
        for kend in range(len(A)):
            distinct[A[kend]] += 1
            if len(distinct) == K + 1:
                print(distinct)
                distinct.pop(A[kstart])
                print(distinct)
                kstart += 1
                i = kstart
            if len(distinct) == K:
                while distinct[A[kstart]] > 1:
                    distinct[A[kstart]] -= 1
                    kstart += 1
                total += kstart - i + 1
        return total



k = 2
arr = [1,2,1,2,3]
s = Solution()
print(s.subarraysWithKDistinct(arr,k))
