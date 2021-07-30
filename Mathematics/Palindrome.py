n = 545
test = n
rev = 0
for i in range(len(str(n))):
    last_digit = int(test % 10)
    rev = rev * 10 + (last_digit)
    test = int(test / 10)
if rev == n:
    print("Palindrome")
else:
    print("Not palindrome")

