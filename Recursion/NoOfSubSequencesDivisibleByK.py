def NoOfSubSequences(ind,ds,sum):
    array = [3,2,4]
    if ind == len(array):
        if sum % 3==0 and sum!=0:
            return 1
        else:
            return 0
    else:
        # Pick
        sum += array[ind]
        ds.append(array[ind])
        left = NoOfSubSequences(ind + 1, ds,sum)
        sum -= array[ind]
        ds.pop()
        # Non Pick
        right = NoOfSubSequences(ind + 1, ds,sum)
        return left + right


ind = 0
ds = []
sum = 0
print(NoOfSubSequences(ind,ds[:],sum))
