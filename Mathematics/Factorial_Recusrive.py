def factorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
         return n * factorial(n-1)

n = 4
print(factorial(n))
