n,u1,d = map(int,input().split())
un = u1 + ( n - 1 ) * d
S = n * (u1 + un) // 2
print(S)