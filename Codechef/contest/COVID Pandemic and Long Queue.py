# COVID Pandemic and Long Queue :--

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = True
    for i in range(n):
        try :
            if a[i] == 1 and a[i+1:i+6].count(1) > 0:
                x = False
                break
        except:
            if a[i] == 1 and a[i+1:].count(1)>0:
                x = False
                break
    if x:
        print("YES")
    else:
        print("NO")
