# Harold : 

for _ in range(int(input())):
    x,y,n = map(int,input().split())
    lst = [y]*x
    for i in range(x,n):
        lst.append(sum(lst[i-x:i]))
        
    print(lst[-1])
        
