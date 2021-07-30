# Using Segmented Sieve Algorithm
'''
step 1:Generate all primes till sqrt(n)
step2: Create dummy array of size (n-m)
step3: Mark all multiples
'''
import math
def segmented_sieve(m,n):
    # Step1: Generate all primes till sqrt(n) using sieve
    primes = sieve(n)
    print(primes)
    # Step2: Create dummy array of size [N-M]
    dummy_array = [True] * (n-m)
    # Step3: Mark all multiples of prime
    for p in primes:
        print("primes",p)
        first_multiple = (m//p) * p
        if first_multiple < m:first_multiple += p
        if p * p > first_multiple:first_multiple = p*p
        if first_multiple > n: break
        for i in range(first_multiple,n+1,p):
            print(i-m)
            dummy_array[i-m] = False
    for i in range(m,n+1):
        if dummy_array[i]:
            print(i,end=' ')

def sieve(n):
    s = int(math.sqrt(n)) +1
    isPrimes = [True] * s
    prime = []
    for i in range(2,s):
        if isPrimes[i]:
            prime.append(i)
            for j in range(i*i,s,i):
                isPrimes[j] = False
    return prime

m = 110
n = 130
segmented_sieve(m,n)
