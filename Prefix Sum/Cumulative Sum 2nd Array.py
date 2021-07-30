n = 5
m = 5
nm_array = [[2,3,4,1,2],[3,1,2,1,3],[1,1,1,2,1],[3,1,2,2,1],[1,2,2,1,2]]
l,r = 1,1
l1,r1 = 3,4
# Brute Force Approach- O(n*m)
sum = 0
for i in range(l,l1+1,1):
    for j in range(r,r1+1,1):
        print(nm_array[i][j])
        sum += nm_array[i][j]
print(sum)

#Prefix 2D Array Sum
# Prefix Array
pre_array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Find subarray addition
l,r,l1,r1 = 0,2,4,4

for i in range(n):
    for j in range(m):
        pre_array[i][j] += nm_array[i][j]
        if i>0 and j==0:
            pre_array[i][j] += pre_array[i-1][j]
        if j>0 and i ==0:
            pre_array[i][j] += pre_array[i][j - 1]
        if i>0 and j>0:
            pre_array[i][j] += pre_array[i-1][j] + pre_array[i][j-1] - pre_array[i-1][j-1]

# Just Printing prefix 2D array
for i in range(n):
    for j in range(m):
        print(pre_array[i][j],end=" ")
    print("\n")

# Finding subarray sum
sum = pre_array[l1][r1]
if l==0 and r>0:
    sum -= pre_array[l1][r-1]
if r==0 and l>0:
    sum -= pre_array[l-1][r1]
if l>0 and r>0:
    sum += pre_array[l-1][r-1]











