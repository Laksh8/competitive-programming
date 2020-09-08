# Crushing Violence : 

for _ in range(int(input())):
    n = int(input())
    boys = list(map(int,input().split()))
    girls = list(map(int,input().split()))
    temp = list(set(girls))
    count = 0
    for i in temp:
        if girls.count(i) > count:
            count = girls.count(i)
    val = 0
    for i in range(n//2):
        x = boys[i]
        boys
        if girls[x-1] != i+1 :
             y = boys[girls[x-1]-1]
             if girls[y-1] == x:
                 val+=2
    print(count,val)
    
        
