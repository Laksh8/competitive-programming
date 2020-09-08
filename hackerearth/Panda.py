# Panda 
'''
def  factorial(n,x):
    temp = x
    for i in range(1,n+1):
        temp = temp * i
    return temp


n,x = map(int,input().split())
print(factorial(n,x))
'''
'''
def factorial(n,x):
    return x if (n==1 or n==0) else n * factorial(n - 1,x);


for _ in range(int(input())):
    n,x = map(int,input().split())
    print(factorial(n,x))
'''

def factorial(n,x):
    if n == 1 or n == 0:
        return x
    return n*factorial(n-1,x)
for _ in range(int(input())):
    n,x = map(int,input().split())
    print(factorial(n,x))
