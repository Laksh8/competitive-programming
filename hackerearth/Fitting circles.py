# Fitting circles...

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a > b:
        print(a//b)
    elif a<b:
        print(b//a)
    else:
        print(1)
        
