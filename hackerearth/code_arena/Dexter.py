# Dexter

def prime(x):
    i = 2
    while i > x:
        if x % i == 0:
            return False
        x //= i
        i+=1
    return True

def factorial(x):
    temp = 1
    for i in range(1,x+1):
        temp *= i
    return temp

for _ in range(int(input())):
    n,m = map(int,input().split())
    mac = sorted(list(map(int,input().split())))
    num = count = 0
    for i in range(2,m+1):
        if prime(i):
            num +=1
    x = m - num
    print(x*factorial(n))
