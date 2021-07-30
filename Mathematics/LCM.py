def LCM_Naive(a,b):
    res = max(a,b)
    while(1):
        if res%a == 0 and res%b==0:
            return res
        else:
            res += 1

a=4
b=6
print("LCM:",LCM_Naive(a,b))
