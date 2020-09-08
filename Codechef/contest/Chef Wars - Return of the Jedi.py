for _ in range(int(input())):
    h,p = list(map(int,input().split()))

    while h>=0 and p>=1:
        
        h -= p
        p /=2
        
    if h <=0 :
        print(1)
    else:
        print(0)
