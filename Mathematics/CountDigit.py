import math
import sys
n = 9235
print(int(math.log10(n)+1))

fact = 1
for i in range(1, 100 + 1):
    fact = fact * i

print(math.log10(fact) + 1)

