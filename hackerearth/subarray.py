# SubArrays :--

temp,result = 0,0
n = 5
arr = [i for i in range(5)]

ans = min(arr)
print(ans)
for i in range(1,n+1):
    for j in range(n):
        if i+j > n: #Subarray Exceeds array bound
            break
        su = 0
        for k in range(j,i+j):
            print(arr[k],end=" ")
        print()
            
