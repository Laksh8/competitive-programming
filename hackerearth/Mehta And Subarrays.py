# Mehta And Subarrays :

n = int(input())
lst = list(map(int,input().split()))

ans = 0
for i in range(1,n+1):
    for j in range(n):
        if i+j > n:
            break
        su = 0
        for k in range(j,i+j):
            su+=lst[k]
        if su > 0:
            val = i
        if su > ans:
            ans = su
if val == 0:
    val = -1
print(ans,val)

