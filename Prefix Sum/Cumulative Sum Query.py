#https://www.spoj.com/problems/CSUMQ/
N = 6
N_array = [2,1,3,4,1,5]
Q = 3
'''
# BruteForce
for i in range(Q):
    start = int(input())
    end = int(input())
    sum = 0
    for j in range(start,end+1):
        sum += N_array[j]
    print(sum)
'''
# Prefix Sum Technique
N = 6
N_array = [2,1,3,4,1,5]
Q = 3
pre_sum = [0] * N
pre_sum[0] = N_array[0]
# o(N) times
for i in range(1,len(N_array)):
    pre_sum[i] = N_array[i] + pre_sum[i-1]
print(pre_sum)
#o(Q)
for i in range(Q):
    start = 2
    end = 5
    if start > 0:
        sum = pre_sum[end] - pre_sum[start-1]
    if start == 0:
        sum = pre_sum[end]
print(sum)




