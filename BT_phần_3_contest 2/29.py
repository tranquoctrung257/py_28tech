n = int(input())
a = list(map(int,input().split()))
tong = 0
for x in a:
    if x % 2 == 0:
        tong+=x
print(tong)