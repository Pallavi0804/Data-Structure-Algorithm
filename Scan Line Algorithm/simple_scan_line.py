def scanline(arr,lrx):
    l = len(arr) + 1
    pre_arr = [0] * l
    for t in lrx:
        pre_arr[t[0]] += t[2]
        pre_arr[t[1]+1] -= t[2]
    bag = 0
    for i in range(len(pre_arr)-1):
        bag += pre_arr[i]
        arr[i] += bag
    return arr



n = 5
arr = [1,5,2,4,4]
lrx = [[0,2,4],[1,4,2],[2,3,5]]
print(scanline(arr,lrx))
