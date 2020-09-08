# Conject-It :

def check(n):
    if n == 0 :
        return False
    elif n == 1:
        return True
    elif n%2==0:
        return check(n//2)
    else:
        return check((n*3)+1)


for _ in range(int(input())):
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")


'''
for _ in range(int(input())):
    n = int(input())
    while(n>1):
        if n%2==0:
            n //=2
            
        else:
            n = (n*3)+1
            
    if n==1:
        print("YES")
    else:
        print("NO")
'''
