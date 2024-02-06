a,b,c,d = map(int,input().split())

print(max(a,b,c,d),min(a,b,c,d))

# hoặc 
min_val, max_val = a,a
if b > max_val: max_val = b
if c > max_val: max_val = c
if d > max_val: max_val = d
if b < min_val: min_val = b
if c < min_val: min_val = c
if d < min_val: min_val = d
print(max_val,min_val)