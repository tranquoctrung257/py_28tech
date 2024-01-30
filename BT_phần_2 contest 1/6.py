n = int(input())

# 1
if n % 2 == 0:
    print("YES")
else:
    print("NO")
#2
if n % 3 == 0 and n % 5 == 0:
    print("YES")
else:
    print("NO")
# 3
if n % 3 == 0 and n % 7 != 0:
    print("YES")
else:
    print("NO")
# 4
if n % 3 == 0 or n % 7 == 0:
    print("YES")
else:
    print("NO")
# 5
if n > 50 and n < 30:
    print("YES")
else:
    print("NO")
# 6
if n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
    print("YES")
else:
    print("NO")
# 7
r = n % 10
if n>= 10 and n <= 99 and (r == 2 or r == 3 or r == 5 or r == 7):
    print("YES")
else:
    print("NO")
# 8
if n <= 100 and n % 23 != 0:
    print("YES")
else:
    print("NO")
# 9
if n < 10 or n > 20:
    print("YES")
else:
    print("NO")
# 10
if r % 3 == 0:
    print("YES")
else:
    print("NO")