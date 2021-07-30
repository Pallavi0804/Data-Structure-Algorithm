class Solution:
    def primePalindrome(self, N):
        N = N+1000
        cnt = 0
        isPrime = [True] * (N+1)
        for i in range(2,N):
            if isPrime[i]:
                cnt +=1
                for j in range(i*i,N+1,i):
                    isPrime[j] = False
        return cnt


N = 6
s = Solution()
print(s.primePalindrome(N))

