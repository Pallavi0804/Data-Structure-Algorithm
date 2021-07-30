dp = {}
def FrogJump2(n,array,k):
    index = 0
    calculate(index,array,n,k,dp)
    print(dp)
    return dp

def calculate(index,array,n,k,dp):
    if index >= n - 1: return 0
    if index in dp: return dp[index]
    cost = 0
    for k1 in range(1,k-1):
        if index + k1 <= n-1:
            cost = min(cost,abs(array[k1] - array[k1 + 1]) + calculate(index+k,array,n,k,dp))
    dp[index] = cost
    return cost

n = 6
k = 4
array = [30,10,60,10,60,50]
print(FrogJump2(n,array,k))
