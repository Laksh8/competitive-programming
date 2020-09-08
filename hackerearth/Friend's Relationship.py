# Friend's Relationship :

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for k in range(2*n-(2*i),2,-1):
            print("#",end="")
        for j in range(i+1):
            print("*",end="")
        print()
            
            
