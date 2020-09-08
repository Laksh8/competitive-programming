# Monk and Rotation :




for _ in range(int(input())):
    n,k = list(map(int,input().strip().split()))
    arr = list(map(int,input().strip().split()))

    k %=n
    
    for i in range(n):
        print(arr[(i + (n-k))%n],end=" ")
        

