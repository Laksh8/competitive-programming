# Sell All the Cars :--

for _ in range(int(input())):
    n = int(input())
    p = sorted(list(map(int,input().split())),reverse=True)
    profit = 0
    for i in range(n):
        
        l = p[i] - i
        if l < 0:
            l = 0
        profit = profit+l
        

    print(profit%1000000007)
