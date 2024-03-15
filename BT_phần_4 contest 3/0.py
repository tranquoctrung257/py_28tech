import math 

# hàm 1 Kiểm tra n là số nguyên tố, nếu đúng in 1, sai in 0.
def ham1(n):
    if n < 2:
        return 0
    else:
        for i in range(2,math.isqrt(n)+1):
            if n % i == 0:
                return 0
        return 1
    
# hàm 2 In tổng chữ số của n.
def ham2(n):
    tong = 0
    while n != 0:
        tong += n%10
        n //=10
    return tong

# hàm 3 In tổng chữ số chẵn của n.
def ham3(n):
    tong = 0
    tamp = 0
    while n != 0:
        tamp = n%10
        if tamp%2 == 0:
            tong += n % 10
        n //=10
    return tong

# hoặc 
# def ham3_(n):
#     tong = 0
#     while n != 0:
#         if n % 10 % 2 == 0:
#             tong += n%10
#         n //=10
#     return tong

# hàm 4 In tổng chữ số của n là số nguyên tố.
def ham4(n):
    tong = 0
    while n != 0:
        r = n % 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            tong += r
        n//=10
    return tong
# hoặc 

# def ham4_(n):
#     tong = 0
#     while n != 0:
#         r = n % 10
#         if ham1(r):
#             tong += r
#         n//=10
#     return tong

# hàm 5 In số lật ngược của n. Ví dụ 123 in 321.
def ham5(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

# hàm 6 In số lượng ước của n là số nguyên tố (làm tương tự như phân tích thừa số ng tố).
# cách 1
def ham6_(n):
    dem = 0
    for i in range(2,n+1):
        if n % i == 0:
            if ham1(i):
                dem+=1
    return dem
def ham6(n):
    dem = 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            dem += 1
            while n % i == 0:
                n //= i
    if n >1:
        dem+=1
    return dem
print(ham6(36))