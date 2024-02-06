n,s = map(int,input().split())

if s % n == 0:
    print(s//n)
else:
    # cộng thêm vì số tiền dư ở đây cho phép từ 1 ==> n
    print(s//n+1)

##########
# tự làm
le = s % n
xu = s // n + le
print(xu)