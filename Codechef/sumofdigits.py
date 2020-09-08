# Sum of Digits :==

def su(a):
    temp = 0
    while a>0:
        temp1 = a%10
        temp = temp+temp1
        a //=10
    print(temp)
    
for i in range(3):
    su(int(input()))
