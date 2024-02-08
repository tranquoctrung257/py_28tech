k2,k3,k5,k6 = map(int,input().split())
k256 =  min(k2,k5,k6)
k32 = min(k3,k2 - k256)
print(k32 * 32 + k256 * 256)