# Coronavirus Spread :--

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ma = 0
    mi = 999999999999
    for i in range(n):
        try:
            if abs(a[i]-a[i+1]) <= 2:
                while(abs(a[i]- a[i+1])<=2 and i<n):
                    count +=1
                    print(count)
                if ma <= count:
                    ma = count
                if mi >= count:
                    mi = count
                count = 0
        
        except:
            pass
    print(mi,ma)
