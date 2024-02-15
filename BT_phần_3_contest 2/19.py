n = int(input())
ans = n // 28
vo = ans 
while vo >= 3:
    temp = vo // 3
    ans += temp
    vo = vo % 3 +temp

print(ans)