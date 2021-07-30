# https://www.codechef.com/COW42020/problems/COW3E/
def modification(k,r1,c1,r2,c2,matrix):
    # Brute Force
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            matrix[i][j] += k
    return matrix[:]

def prefix_sum(r1, c1, r2, c2,pre_sum):
    sum = pre_sum[r2][c2]
    if r1>0:
        sum -= pre_sum[r1-1][c2]
    if c1>0:
        sum -= pre_sum[r2][c1-1]
    if r1>0 and c1>0:
        sum += pre_sum[r1-1][c1-1]
    return sum

n,m,u,q = map(int, input().rstrip().split())
matrix = []
scan_line = [0] * (len(matrix)+1)
for i in range(n):  # A for loop for row entries
    a = list(map(int, input().rstrip().split())) # A for loop for column entries
    matrix.append(a)

for i in range(u):
    modified_array = []
    k, r1, c1, r2, c2 = map(int, input().rstrip().split())
    modified_array = modification(k,r1,c1,r2,c2,matrix[:])

    print("Modified Array")
    for i in range(n):
        for j in range(m):
            print(modified_array[i][j], end="")
        print("\n")

# Prefix Sum Array
pre_sum = []
for i in range(n):
    a = [0] * m
    pre_sum.append(a)

for i in range(n):
    for j in range(m):
        pre_sum[i][j] += modified_array[i][j]
        if i > 0 and j == 0:
            pre_sum[i][j] += pre_sum[i-1][j]
        if j > 0 and i == 0:
            pre_sum[i][j] += pre_sum[i][j - 1]
        if i > 0 and j > 0:
            pre_sum[i][j] += pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]

print("Prefix Array")
for i in range(n):
    for j in range(m):
        print(pre_sum[i][j],end=" ")
    print("\n")

for i in range(q):
    r1, c1, r2, c2 = map(int, input().rstrip().split())
    print(prefix_sum(r1,c1,r2,c2,pre_sum[:]))



