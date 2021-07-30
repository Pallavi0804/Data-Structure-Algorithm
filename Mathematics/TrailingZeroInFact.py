def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def Trainling_Zero_Naive_solution(n):
    trail = 0
    for i in range(len(str(n))):
        last_digit = n % 10
        n = n / 10
        if last_digit == 0:
            trail +=1
        else:
            break
    return trail

def Trainling_Zero_Efficient_solution(n):
    trail = 0
    i = 5
    while(i<=n):
        trail = trail + int(n/i)
        i=i*5
    return trail

n = 5
fact = factorial(n)
print("Factorial:",fact)
print("Trainling Zeros are with Naive_solution:",Trainling_Zero_Naive_solution(fact))
print("Trainling Zeros are with Efficient_solution:",Trainling_Zero_Efficient_solution(n))


