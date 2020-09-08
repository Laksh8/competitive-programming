#Racing Horses :--  

t = int(input())
diff = 5000
for i in range(t):
    inp = int(input())
    lst = list(map(int,input().split()))
    for j in range(inp):
        for k in range(inp):
            if j !=k:
                if lst[j]-lst[k] > 0:
                    if lst[j]-lst[k]< diff:
                        diff = lst[j]-lst[k]
            else:
                if j != k:
                    if -(lst[j]-lst[k]) <diff:
                        diff = -(lst[j]-lst[k])

print(diff)
