def subsequence_sum(ind,ds,sum,k):
    array = [3,2,4]
    if ind == len(array):
        if sum % k == 0 and len(ds) > 0:
            print(ds)
    else:
        # Pick
        sum += array[ind]
        ds.append(array[ind])
        subsequence_sum(ind+1,ds,sum,k)
        # Non Pick
        sum -= array[ind]
        ds.pop()
        subsequence_sum(ind+1,ds,sum,k)


ind = 0
ds = []
sum = 0
k = 3
subsequence_sum(ind,ds,sum,k)
