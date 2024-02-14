n = int(input())
tong = 0
for i in range(1,n+1):
    if i % 2 == 0:
        tong+=i
    else:
        tong-=i
print(tong)

# hoặc
if n % 2 == 0:
    print(n//2)
else:
    print((n-1)/2-n)