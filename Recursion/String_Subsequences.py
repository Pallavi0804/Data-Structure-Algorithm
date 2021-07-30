def find_Subsequences(ind,s,ds):
    if ind == len(s):
        print(ds)
        return
    # Pick
    ds.append(s[ind])
    find_Subsequences(ind+1,s,ds)
    ds.pop()
    # Non Pick
    find_Subsequences(ind+1,s,ds)

s = 'ABC'
ds = []
find_Subsequences(0,s,ds[:])
