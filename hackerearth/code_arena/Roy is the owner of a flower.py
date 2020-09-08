# Roy is the owner of a flower :

for _ in range(int(input())):
    n,p = map(int,input().split())
    lst = []
    for i in range(n):
        x,y = map(int,input().split())
        lst.append([x/y,x,y])
    lst.sort(reverse=True)
    a=b=0
    for i in lst:
        if p>i[2]:
            b = b+p-i[2]+i[1]
            print(b,p-i[2],i[1])
            p -=i[2]
            a+=i[2]
            
    print(a,b)
    

'''
for _ in range(int(input())):
    n,p = map(int,input().split())
    lst = []
    for i in range(n):
        x,y = map(int,input().split())
        lst.append([x/y,x,y])
    lst.sort(reverse=True)
    print(lst)
    a =b=0
    for i in lst:
        if p>i[2]:
            b = b+p-i[2]+i[1]
            p -= i[2]
            a += i[2]

     
    
'''
