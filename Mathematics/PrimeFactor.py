import math
def PrimeFactor(n):
    print("Naive Solution")
    for i in range(2,n):
        if(isPrime(i)):
            x = i
            while(n%x==0):
                print(i,end=' ')
                x = x * i

def EfficientPrimeFactor(n):
    print("\nEfficient Solution")
    if (n<=1):
        return
    for i in range(2,int(math.sqrt(n))):
        while(n%i==0):
            print(i,end=' ')
            n=n//i
        if n == 1:
            break

    if (n>1):
        print(int(n))

def MoreEfficientPrimeFactor(n):
    print("\nMore Efficient solution")
    if (n<=1):
        return
    while(n%2==0):
        print(2,end=' ')
        n = n // 2
    while(n%3==0):
        print(3,end=' ')
        n = n // 3
    for i in range(5,int(math.sqrt(n))+1,6):
        #print("working")
        while(n%i==0):
            print(i,end=' ')
            n = n // i
        while(n%(i+2)==0):
            print(i+2,end=' ')
            n = n //(i+2)
    if (n>3):
        print(n)



def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0:
            return False
    return True

n = 450
PrimeFactor(n)
EfficientPrimeFactor(n)
MoreEfficientPrimeFactor(n)
