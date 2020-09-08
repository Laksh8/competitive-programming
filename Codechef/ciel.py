from random import randint

a,b = map(int,input().split())
c = a-b
ran = randint(1,9)
mod = c%10
while True:
    if ran != mod:
        c //=10
        c = c*10 +ran
        break
print(c)
