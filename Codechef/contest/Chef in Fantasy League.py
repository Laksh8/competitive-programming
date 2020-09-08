# Chef in Fantasy League : 

for _ in range(int(input())):
    n,s = map(int,input().strip().split(" "))
    p = list(map(int,input().strip().split(" ")))
    pos = list(map(int,input().strip().split(" ")))
    f = []
    d = f.copy()
    for i in range(n):
        if pos[i] == 1:
            f.append(p[i])
        else:
            d.append(p[i])
    f.sort();d.sort()
    if s+f[0]+d[0] <= 100:
        print("yes")
    else:
        print("no")
    
