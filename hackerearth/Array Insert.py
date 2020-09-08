# Array Insert :-

n,q = map(int,input().split())
a = list(map(int,input().split()))
for i in range(q):
    x,l,r = map(int,input().split())
    if x == 1:
        a[l] = r
    else:
        print(sum(a[l:r+1]))
