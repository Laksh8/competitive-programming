# Unit GCD : --

for _ in range(int(input())):
    n = int(input())
    i = 4
    if n == 1:
        print(1)
        print(1,1)
    elif n == 2:
        print(1)
        print(2,1,2)
    else:
        print(n//2)
        
        print(3,1,2,3)
        while(i<=n):
            
            if i<n:
                print(2,i,i+1)
            else:
                print(1,i)
            i+=2
        
        
            
