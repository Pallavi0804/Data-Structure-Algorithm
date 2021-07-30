def Find_SubSequences(ind,ds):
    array = [3, 5, 6]
    if ind == len(array):
        print(ds)
    else:
        #Pick
        ds.append(array[ind])
        Find_SubSequences(ind+1,ds)
        ds.pop()
        #Non Pick
        Find_SubSequences(ind+1,ds)

ind = 0
ds = []
Find_SubSequences(ind,ds[:])
