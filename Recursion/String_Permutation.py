def string_permutation(s,ds,hash):
    if len(ds) == len(s):
        print(ds)
        return
    for i in range(len(s)):
        if hash[i] == False:
            ds.append(s[i])
            hash[i] = True
            string_permutation(s,ds,hash)
            ds.pop()
            hash[i] = False

s = 'ABC'
ds = []
hash = [False] * len(s)
string_permutation(s,ds[:],hash)
