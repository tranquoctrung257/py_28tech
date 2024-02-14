# tổng ước

import math


n = int(input())
# tong = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         tong+=i
# print(tong)

tong = 0
for i in range(1,math.isqrt(n)+1):
    if n % i == 0:
        tong += i
        if i != n //i :
            tong += n // i
print(tong)