# Binary Queries :--

global narr

def check(lst):
    if narr[lst[2]-1]==1:
        return("ODD")
    else:
        return("EVEN")
        
  
    
n,q = map(int,input().split())
narr = list(map(int,input().strip().split()))

for i in range(q):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        if narr[lst[1]-1] == 0:
            narr[lst[1]-1] = 1
        else:
            narr[lst[1]-1] = 0
    else:
        print(check(lst))

