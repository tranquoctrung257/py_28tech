a,b,c,n = map(int,input().split())
if (n + a + b + c ) % 3 == 0:
    tmp = (n + a + b + c ) // 3
    if tmp >= a and tmp >= b and tmp >= c:
        print("Yes")
    else:
        print("NO")
else:
    print("NO")