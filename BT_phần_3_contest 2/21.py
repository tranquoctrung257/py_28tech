n = int(input())

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print("")
print("")


for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
print()


for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print(" ")
print()
"""
1 1 1 1 1
2       2
3       3
4       4
5 5 5 5 5
"""
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print(" ")