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

# hàm 7 In ước nguyên tố lớn nhất của n (làm tương tự như phân tích thừa số ng tố).
def ham7(n):
    res = -1
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            res = i 
            while n % i == 0:
                n //= i 
    if n > 1:
        res = n
    return res

# hàm 8 Kiểm tra nếu n tồn tại ít nhất 1 số 6, nếu đúng in 1, sai in 0.
def ham8(n):
    while n != 0:
        if n % 10 == 6 :
            return 1
        n//=10
    return 0

# hàm 9 Kiểm tra nếu tổng chữ số của n chia hết cho 8, nếu đúng in 1, sai in 0.
def ham9(n):
    tong = 0
    while n != 0:
        tong += n%10
        n//=10
    if tong % 8 == 0:
        return 1
    else:return 0

# hàm 10 Tính tổng giai thừa các chữ số của n và in ra. Ví dụ n = 123, tổng = 1! + 2! +3!
def ham10(n):
    tong = 0
    while n != 0:
        tong += math.factorial(n%10)
        n //= 10
    return tong

# hàm 11 Kiểm tra n có phải chỉ được tạo bởi 1 số hay không? Ví dụ 222, 333, 99999. Đúng in ra 1, sai in ra 0.
def ham11(n):
    donvi = n % 10
    while n != 0:
        if donvi != n % 10:
            return 0
        n//=10
    return 1

# hàm 12 Kiểm tra n có phải có chữ số tận cùng là lớn nhất hay không, tức là không có chữ số nào của n lớn hơn chữ số hàng đơn vị của nó. nếu đúng in 1, sai in 0.
def ham12(n):
    donvi = n % 10
    while n != 0:
        if n % 10 > donvi:
            return 0
        n //= 10
    return 1

# hàm 13 In tổng lũy thừa chữ số của n với số mũ là số chữ số. ví dụ 123 thì tính 1^3+2^3+3^3.
# ví dụ 1234 => 1^4+2^4+3+4^4
def ham13(n):
    m = n
    cnt = 0
    while n != 0:
        cnt += 1
        n//= 10
    tong = 0
    while m != 0:
        tong += (m % 10 ) ** cnt
        m//=10
    return tong

if __name__ =="__main__":
    n = int(input())
    print(ham1(n))
    print(ham2(n))
    print(ham3(n))
    print(ham4(n))
    print(ham5(n))
    print(ham6(n))
    print(ham7(n))
    print(ham8(n))
    print(ham9(n))
    print(ham10(n))
    print(ham11(n))
    print(ham12(n))
    print(ham13(n))    
