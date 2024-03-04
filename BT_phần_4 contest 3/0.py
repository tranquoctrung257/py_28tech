# Cho số nguyên n không âm. Viết hàm xử lý các yêu cầu sau

# Kiểm tra n là số nguyên tố, nếu đúng in 1, sai in 0.
# In tổng chữ số của n.
# In tổng chữ số chẵn của n.
# In tổng chữ số của n là số nguyên tố.
# In số lật ngược của n. Ví dụ 123 in 321.
# In số lượng ước của n là số nguyên tố (làm tương tự như phân tích thừa số ng tố).
# In ước nguyên tố lớn nhất của n (làm tương tự như phân tích thừa số ng tố).
# Kiểm tra nếu n tồn tại ít nhất 1 số 6, nếu đúng in 1, sai in 0.
# Kiểm tra nếu tổng chữ số của n chia hết cho 8, nếu đúng in 1, sai in 0.
# Tính tổng giai thừa các chữ số của n và in ra. Ví dụ n = 123, tổng = 1! + 2! +3!
# Kiểm tra n có phải chỉ được tạo bởi 1 số hay không? Ví dụ 222, 333, 99999. Đúng in ra 1, sai in ra 0.
# Kiểm tra n có phải có chữ số tận cùng là lớn nhất hay không, tức là không có chữ số nào của n lớn hơn chữ số hàng đơn vị của nó. nếu đúng in 1, sai in 0.
# In tổng lũy thừa chữ số của n với số mũ là số chữ số. ví dụ 123 thì tính 1^3+2^3+3^3.
import math
def ngto(n):
    if n < 2 :return "0"

    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return "0"
    return 1
def ham2(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n//= 10
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
        if r == 2 or r == 3 or r == 5 or r == 5:
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
    
