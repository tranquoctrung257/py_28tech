a,b,c,d = map(int,input().split())
if b % a == 0:
    q = b // a
    if b * q == 0 and c * q == d:
        print("YES")
    else:
        print("NO")
else:
    print("NO")