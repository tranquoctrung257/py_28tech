n = int(input())

nam = n // 365
n = n % 365
tuan = n // 7
n = n % 7
print(nam,tuan,n)
 