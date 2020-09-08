# Check Prime :--
def prime(a):
    i=2
    while(a//i and i<a):
        if a%i==0:
            return False
        i+=1
    return True

# Write your code here
q = []
for _ in range(int(input())):
    q.append(int(input()))
for x in q:
    su = 0
    j = 2
    for i in range(x):
        while True:
            if prime(j):
                su+=j
                j+=1
                break
            j+=1
    print(su)

'''
def check(a):
    i = 2
    while(a//i and i<a):
        if a%i==0:
            return False
        i+=1
    return True

def sumDigit(x):
    temp = 0
    while(x>0):
        temp = temp+x%10
        x//=10
    return temp

for i in range(1,1000):
    if check(i):
        if sumDigit(i)==23:
            print(i)
'''
