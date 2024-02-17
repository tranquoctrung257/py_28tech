"""
*
**
***
****
*****
"""
n = int(input())
for i in range(1,n+1):
    # dòng i lặp i lần
    for j in range(i):
        print("*",end="")
    print()
print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print()

for i in range(1,n+1):
    # dòng 1 i : j <= n - i : cách,*
    for j in range(1,n+1):
        if j <= n - i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if j < i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
print()
# i là chỉ số dòng
# j là chỉ số cột

for i in range(1,n+1):
    # dòng i lặp i lần
    for j in range(1,i+1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

