n = int(input())
gt = 1
tong = 0
for i in range(1,n+1):
    gt *=i
    tong += gt
print(tong)