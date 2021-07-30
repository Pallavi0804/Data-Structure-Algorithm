import math
def All_Divisors_NaiveSolution(n):
   print("Naive Solution")
   for i in range(1,n+1):
       if n%i==0:
           print(i,end=' ')

def All_Divisors_EfficientSolution(n):
    print("\nEfficient Solution")
    divisors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            print(i,end=' ')
            if(i!=n/i):
                divisors.insert(0,n//i)

    print(*divisors, sep=" ")


n = 30
All_Divisors_NaiveSolution(n)
All_Divisors_EfficientSolution(n)
