#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1474
#Brute Force
def DigitsPrime(t1,t2):
    count = 0
    for i in range(t1,t2+1):
        if isPrime(i) is True:
            no = i
            sum = 0
            while(no!=0):
                sum += no % 10
                no = no // 10
            if isPrime(sum) is True:
                count += 1
    return count

def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        #print("i",i)
        if n % i == 0 or n % (i+2)==0:
            return False
    return True


t1, t2 = 100,10000
print(DigitsPrime(t1,t2))
'''n = int(input())
for i in range(n):
    t1, t2 = map(int, input().rstrip().split())
    print(DigitsPrime(t1,t2))'''

