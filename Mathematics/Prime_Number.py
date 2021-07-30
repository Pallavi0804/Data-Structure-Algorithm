import math
def Prime_Naive(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def Prime_Efficient(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def Prime_More_Efficient(n):
    if n == 1:
        return False
    if n ==2 or n==3:
        return True
    if n % 2==0 or n%3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1,6):
        if n % i == 0:
            return False
    if n>3:
        return False

    return True


n=1000000007
#res = Prime_Naive(n)
#res = Prime_Efficient(n)
res = Prime_More_Efficient(n)
if res == False:
    print(n," is not prime")
else:
    print(n," is prime")
print((math.pow(10, 9) + 7))
