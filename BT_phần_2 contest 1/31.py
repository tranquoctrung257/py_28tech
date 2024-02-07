# a1,a2,a3,b1,b2,b3 = map(int,input().split())
# n = int(input())
# cup = a1+a2+a3
# hc = b1+b2+b3
# ke1,ke2 = 0,0
# if cup % 5 == 0:
#     ke1 = cup // 5
# else:
#     ke1 = cup // 5 + 1
# if hc % 10 == 0:
#     ke2 = hc // 10
# else:
#     ke2 = hc // 10 +1
# if ke1 + ke2 <= n:
#     print("YES")
# else:
#     print("NO")

# Đọc dữ liệu đầu vào
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())

# Tính tổng số lượng cúp và huy chương
total_cups = a1 + a2 + a3
total_medals = b1 + b2 + b3

# Kiểm tra xem có thể sắp xếp tất cả các phần thưởng vào kệ hay không
# với các ràng buộc đã cho
if total_cups <= n and total_medals <= 10 * n and total_cups + total_medals <= 5 * n:
    print("YES")
else:
    print("NO")