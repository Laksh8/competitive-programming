# Lead Game :

ma = [1,0]
p1 , p2 = 0,0
for _ in range(int(input())):
    a , b  = map(int,input().split())
    p1 += a
    p2 += b
    if p1 - p2 > 0:
        if ma[1] < p1-p2:
            ma[0],ma[1] = 1,p1-p2
    elif p1-p2 < 0:
        if abs(p1-p2) > ma[1]:
            ma[0],ma[1] =2,abs(p1-p2)
for i in ma:
    print(i,end=" ")
