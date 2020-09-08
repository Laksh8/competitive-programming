# Easy Going.(Very Easy) :--


for _ in range(int(input())):
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    dif = max(lst)-min(lst)
    mi = mx = 0
    for i in range(dif):
        mi += lst[i]
        mx += lst[-1-i]
    print(mx-mi)
    
