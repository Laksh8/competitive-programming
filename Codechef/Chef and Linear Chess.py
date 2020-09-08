# Chef and Linear Chess :

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    p = list(map(int,input().split()))
    temp = [-1,0]
    for i in range(n):
        if k % p[i] == 0 and p[i] > temp[0]:
            temp = [p[i],k // p[i]]

    print(temp[0])
            
