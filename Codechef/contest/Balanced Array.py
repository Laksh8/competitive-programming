# Balanced Array :--

for _ in range(int(input())):
    n = int(input())
    if n % 4 == 0:
        print("YES")
        su = sum([i for i in range(2,n+1,2)])
        for i in range(2,n+1,2):
            print(i,end=" ")
        for i in range(1,n-1,2):
            print(i,end=" ")
            su -= i
        print(su)
    else:
        print("NO")

            
