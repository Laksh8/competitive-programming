# Another Birthday Present! :--

for _ in range(int(input())):
    n,k = tuple(map(int,input().split()))
    arr = list(map(int,input().split()))
    lst = sorted(arr)

    for i in range(n):
        try:
            if arr[i] >= arr[k+i]:
                arr[i] ,arr[k+i] = arr[k+i],arr[i]
                
        except:
            break
    
    if arr == lst:
        print("yes")
    else:
        print("no")
