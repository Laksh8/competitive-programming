# Micro and Array Update

for _ in range(int(input())):
    n ,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    temp = a[0]
    x= 0
    while temp<k:
        temp +=1
        x +=1

    print(x)
        
