# matrix of size n
for i in range(int(input())):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(str,input())))

for i in range(n):
    for j in range(n):
        if lst[i][j] == '*':
            x,y = i,j
print(abs(x-n//2)+abs(y-n//2))
