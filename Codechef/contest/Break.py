# Break :


t,s = map(int,input().split())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    print(a,b)
    x = True
    for i in range(n):
        for j in range(i,n):
            if a[i]<b[j]:
                b[i],b[j] = b[j],b[i] 
                x = True
            else:
                
                x = False
    if x:
        print("YES")
    else:
        print("NO")
            
