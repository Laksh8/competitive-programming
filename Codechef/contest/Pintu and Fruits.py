# Pintu and Fruits :


for _ in range(int(input())):
    n,m = map(int,input().split())
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        try :
            dic[f[i]].append(p[i])
        except :
            dic[f[i]] = []
            dic[f[i]].append(p[i])
    
    mi = sum(dic[f[0]])
    for key,value in dic.items():
        if mi > sum(value):
            mi = sum(value)
    print(mi)
