n = int(input())
# n = 5
"""
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""
dem = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(dem,end=" ")
        dem+=1
    print()
print()
for i in range(1,n+1):
    ktao = i 
    for j in range(1,n+1):
        print(ktao,end=" ")
        ktao+=1
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n - i:
            print("~",end=" ")
        else:print(i,end=" ")
    print()
print()

for i in range(1,n+1):
    ktao = i 
    kc = n - 1
    for j in range(i):
        print(ktao,end=" ")
        ktao+=kc
        kc-=1
    print()