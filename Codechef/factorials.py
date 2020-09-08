def fac(a):
    temp = 1
    for i in range(2,a+1):
        temp = temp *i
    print(temp)
    
t = int(input())

for i in range(t):
    fac(int(input()))
