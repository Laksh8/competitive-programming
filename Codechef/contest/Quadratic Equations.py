# Quadratic Equations :

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    d=(b**2) - (4*a*c)
    if d > 0:
        x = (-b+(d**(1/2)))/(2*a)
        if int(x) == x:
            print(int(x),end=" ")
        else:
            print("%.8f"%x,end=" ")
        x = (-b-(d**(1/2)))/(2*a)
        if int(x) == x:
            print(int(x))
        else:
            print("%.8f"%x)
        
    elif d == 0:
        x = -b/(2*a)
        if int(x)==x:
            print(int(x),' ',int(x))
        else:
            print("%.8f %.8f"%(x,x))
    else:
        print("No REAL roots found")
