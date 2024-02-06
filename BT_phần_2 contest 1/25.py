n = int(input())
ans = n // 100
n %= 100
ans += n // 20
n %= 20
ans += n // 10 
n %= 10
ans += 5 // n
n %= 5 
ans += n
print(ans)

