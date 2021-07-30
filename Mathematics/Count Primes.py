# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n):
        isPrime = [True] * (n+1)
        cnt = 0
        for i in range(2,n):
            if isPrime[i]:
                cnt += 1
                for j in range(i*i,n+1,i):
                    isPrime[j] = False
        return cnt

s = Solution()
print(s.countPrimes(10))
