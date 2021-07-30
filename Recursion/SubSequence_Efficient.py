# Formation of Sequence at every step
# Improved version of pick and non pick technique
def Find_SubSequences(ind,ds):
    array = [1,2,2]
    print(ds)
    if ind == len(array):
        return
    else:
        for i in range(ind,len(array)):
            ds.append(array[i])
            Find_SubSequences(i+1,ds[:])
            ds.pop()
ind = 0
ds = []
Find_SubSequences(ind,ds[:])

