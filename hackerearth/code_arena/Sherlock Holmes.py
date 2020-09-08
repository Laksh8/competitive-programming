def check(n,m,lst,x):
        for i in range(n):
            if x in lst[i]:
                return "%d %d"%(i,lst[i].index(x))
        return "%d %d"%(-1,-1)

        

# Write your code here



n,m = map(int,input().split())
lst = [] 
for i in range(n):
    lst.append(list(map(int,input().split())))

for i in range(int(input())):
    x = int(input())
    print(check(n,m,lst,x))
    

'''
def check(n,m,lst,x):
        for i in range(n):
            if x in lst[i]:
                return "%d %d"%(i,lst[i].index(_))
        return "%d %d"%(-1,-1)

        

# Write your code here



n,m = map(int,input().split())
lst = [] 
for i in range(n):
    lst.append(list(map(int,input().split())))
x = []
for i in range(int(input())):
    x.append(int(input()))

for _ in x:
    print(check(n,m,lst,_))
    
'''
