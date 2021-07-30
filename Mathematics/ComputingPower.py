def ComputingPower_NaiveSolution(x,n):
    res = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            res = res * x
    return res

def ComputingPower_EfficientSolution(x,n):
    res = 1
    if n == 0:
        return 1
    temp = ComputingPower_EfficientSolution(x,n//2)
    temp = temp * temp
    if n%2 == 0:
        return temp
    else:
        return temp * x

def ComputingPower_MoreEfficient(x,n):
    res = 1
    while(n>0):
        if n % 2 != 0:
            res = res * x
        x = x * x
        n = n//2
    return res

x = 4
n = 5
print(ComputingPower_NaiveSolution(x,n))
print(ComputingPower_EfficientSolution(x,n))
print(ComputingPower_MoreEfficient(x,n))
