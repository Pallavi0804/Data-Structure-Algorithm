# https://atcoder.jp/contests/dp/tasks/dp_a

dp = {}
def FrogJump(n,array):
    index = 0
    calculate(index,array,n,dp)
    # for key in dp:
    #     print(dp[key], end=' ')
    return dp[0]

def calculate(index,array,n,dp):
    if index >= n-1:return 0
    if index in dp:return dp[index]

    first_cost = abs(array[index]-array[index+1]) + calculate(index+1,array,n,dp)
    if index+2 <= n-1:
        second_cost = abs(array[index]-array[index+2]) + calculate(index+2,array,n,dp)
        dp[index] = min(first_cost, second_cost)
    else:
        dp[index] = first_cost

    return dp[index]

n = 6
array = [30,10,60,10,60,50]
print(FrogJump(n,array))
