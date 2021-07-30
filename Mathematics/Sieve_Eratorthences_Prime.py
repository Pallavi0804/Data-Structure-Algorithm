def sieve(n):
    isPrime = [True] * (n+1)
    for i in range(2,n):
        if isPrime[i]:
            print(i)
            for j in range(i*i,n+1,i):
                isPrime[j] = False


n = 25
sieve(n)
