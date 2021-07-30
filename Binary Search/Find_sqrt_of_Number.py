# Find SQRT of given Number, n = 25, ans should be 5
# n = 36, ans should be 6
def sqrt_brute_force(n):
    for i in range(n):
        if i * i <= n:
            sqrt = i
    return sqrt

def sqrt_binary_search(n):
    low = 1
    high = n
    sqrt = 0
    while low <= high:
        mid = (low+high)//2
        if mid*mid == n:
            sqrt = mid
            break
        elif mid*mid < n:
            sqrt = mid
            low = mid + 1
        elif mid*mid > n:
            high = mid - 1

    return sqrt


n = 25
print(sqrt_brute_force(n))
print(sqrt_binary_search(n))
