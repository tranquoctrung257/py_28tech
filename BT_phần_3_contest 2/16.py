n = int(input())
dem = 0
if n == 0:
    print(1)
else:
    while n != 0:
        dem+=1
        n//=10
print(dem)