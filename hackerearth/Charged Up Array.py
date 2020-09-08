# Charged Up Array :
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    tol = 2**(n-1)
    su = 0
    for i in lst:
        if i >= tol:
            su +=i
    print(su)






































'''
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    q = 2**(n-1)
    sumi=0
    print(q)
    for j in l:
        
        if j>=q:
            print(j,end =" ")
            sumi+=j
    print('\n'+str(sumi%1000000007))
'''
