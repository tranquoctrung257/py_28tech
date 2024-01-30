import math
x1,x2,y1,y2 = map(int,input().split())
res = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
print("%.2f"%res)