n = int(input())

for i in range(1,n+1):
    print(i,end=" ")
print()
for j in range(n,-1,-1):
    print(j,end=" ")
print()
for x in range(0,n+1):
    if x % 2 == 0:
        print(x,end=" ")
print()
for z in range(1,n+1):
    if z % 2 != 0:
        print(z,end=" ")
    # hoặc
# for i in range(1,n+1,2):
#     print(i,end=" ")
print()

for k in range(0,n,4):
    print(k,end=" ")
print()
# trong bẩng mã ascii kí tụ in thường từ 97 đến 122
for i in range(0,n):
    print(chr(97+i),end= " ")
print()

for i in range(122-n+1,123):
    print(chr(i),end=" ")
   