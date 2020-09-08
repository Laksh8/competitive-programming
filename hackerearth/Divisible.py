# Divisible : 

n = int(input())

arr = input().split()

temp = ""
for i in range(n):
    if i < n//2:
        temp += arr[i][0]
    else:
        temp += arr[i][-1]
if int(temp) % 11 == 0:
    print("OUI")
else:
    print("NON")
