def sliding_window(n,k,arr):
    #Find Prefix array
    pre_arr = [0] * n
    pre_arr[0] = arr[0]
    for i in range(1,len(pre_arr)):
        pre_arr[i] += pre_arr[i-1] + arr[i]
    # Sliding window technoque
    max = 0
    for i in range(0,(n-k)+1):
        l = i
        r = i + (k-1)
        if l ==0: sum = pre_arr[r]
        if l>0: sum = pre_arr[r] - pre_arr[l-1]
        if sum>max:
            max = sum
    return max

def more_efficient_sliding_window(n,k,arr):
    max = 0
    sum = 0
    for i in range(0,k):
        sum += arr[i]
    for i in range(1,(n-k)+1):
        if sum>max: max=sum
        l = i
        r = i + (k-1)
        sum += arr[r] - arr[l-1]
        if sum>max: max=sum

    return max


n = 6
k = 4
arr = [1,5,4,4,3,2]
print(sliding_window(n,k,arr))
print(more_efficient_sliding_window(n,k,arr))
