n = int(input())
fac = 1

for i in range(1,n+1):
    fac*=i
print(fac)

# hoặc 
import math 
print(math.factorial(n))