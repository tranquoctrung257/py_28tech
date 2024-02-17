import math
n = int(input())
s = 0
for i in range(n):
    s += 1/math.factorial(i)
print("{:.4f}".format(s))