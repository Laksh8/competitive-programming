# Leaked Answers :

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    x = []
    for i in range(n):
        c = list(map(int,input().split()))
        x.append(max([[c.count(i),i] for i in range(1,m+1)]))
    for i in x:
        print(i[1],end=" ")
    print()
        
