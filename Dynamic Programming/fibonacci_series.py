dp = {1:1,2:1}
def fibo(n):
    if n <=1:
        return n
    if n not in dp.keys():
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

n = 8
fibo(n)

for key in dp:
    print(dp[key],end=' ')

