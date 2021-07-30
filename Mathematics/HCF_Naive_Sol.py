def HCF_Naive(a,b):
    hcf = min(a,b)
    if int(max(a,b)%hcf)==0:
        return hcf
    else:
        for i in range(hcf-1,1,-1):
            if int(max(a,b)%i) == 0 and int(min(a,b)%i==0):
                hcf = i
                break
        if hcf == min(a,b):
            return 1
        else:
            return hcf

def HCF_Efficient(a,b):
    if(b==0):
        return a
    else:
        #temp = a % b
        return HCF_Efficient(b,a%b)

a=15
b=10
print("HCF Naive:",HCF_Naive(a,b))
print("HCF Efficient: ",HCF_Efficient(a,b))
