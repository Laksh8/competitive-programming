# Monk and Inversions :

for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int,input().split())))
    count = 0
    for i in range(n):
        for j in range(n):
            for x in range(i,n):
                for y in range(j,n):
                    if lst[i][j] > lst[x][y] : count +=1
    print(count)
        
