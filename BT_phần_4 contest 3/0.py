
import math
def ham1(n):
    if n < 2 :
        return 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1
def ham2(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

def ham3(n):
    tong = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            tong += n % 10
        n//= 10
    return tong

def ham4(n):
    tong = 0
    while n != 0:
        r = n % 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            tong +=r
        n //= 10
    return tong
def ham5(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
def ham6(n):
    dem = 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            dem +=1
            while n % i == 0:
                n //= i
    if n > 1:
        dem+=1
    return dem
def ham7(n):
    res = -1
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            res = i
            while n % i == 0:
                n //= i 
    if n > i:
        res = n 
    return res

def ham8(n):
    while n != 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
def ham9(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    if tong % 8 == 0:
        return 1
    else:
        return 0
def ham10(n):
    tong = 0
    while n != 0:
        tong += math.factorial(n % 10)
        n //= 10
    return tong
def ham11(n):
    donvi = n % 10
    while n != 0:
        if donvi != n % 10:
            return 0
        n //= 10
    return 1
def ham12(n):
    donvi = n % 10
    while n != 0:
        if n % 10 > donvi:
            return 0
        n //= 10
    return 1

def ham13(n):
    m = n 
    cnt = 0
    while n != 0:
        cnt +=1
        n //= 10
    tong = 0
    while m != 0:
        tong += (m % 10) ** cnt
        m //= 10
    return tong

if __name__ == "__main__":
    n = (int(input()))
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