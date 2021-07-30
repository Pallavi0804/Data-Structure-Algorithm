def findXorLtoR(l,r):
    return findXor(r) ^ findXor(l-1)

def findXor(n):
    if n % 4 == 1: return 1
    if n % 4 == 2: return n+1
    if n % 4 == 3: return 0
    if n % 4 == 0: return n


l = 5
r = 12
print(findXorLtoR(l,r))
