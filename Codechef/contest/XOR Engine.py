# XOR Engine :

def fun(i):
    count = 0
    while(i):
        count += i&1;
        i>>=1;
    return count
    
for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    even = odd = 0
    lst = []
    for i in range(n):
            lst.append(fun(a[i]))
    for __ in range(q):
        p = fun(int(input()))
        for i in range(n):
            if (lst[i] %2 == 0 and p%2==0) or (lst[i] %2 != 0 and p%2!=0):
                even += 1
            elif (lst[i]%2==0 and p%2 !=0) or (lst[i]%2!=0 and p%2 ==0):
                odd+=1
        print(even,odd)
