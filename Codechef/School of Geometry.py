# School of Geometry :

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().strip().split()));a.sort()
    b = list(map(int,input().strip().split()));b.sort()
    s = 0
    for i in range(n):
        s += min(a[i],b[i])
    print(s)
