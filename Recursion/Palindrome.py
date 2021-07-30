def Palindrome(str,start,end):
    if end>start:
        if str[start] == str[end]:
            print(Palindrome(str,start+1,end-1))
        else:
            return "Not Palindrome"
    else:
        return "Palindrome"

str = "madam"
start = 0
end = len(str)
print(Palindrome(str,start,end-1))
