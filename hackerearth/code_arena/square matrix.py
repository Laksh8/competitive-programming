for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(str,input())))
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]=="*":
                count = abs(i-(n//2))
                count+= abs(j-(n//2))
                break
    print(count)
