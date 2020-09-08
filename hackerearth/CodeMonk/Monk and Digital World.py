# Monk and Digital World

def check(a,b):

    for i in set(a):
        if a.count(i) != b.count(i):
            return False
    return True

n = int(input())
a = list(map(str,input()))
b = list(map(str,input()))

if check(a,b):
    print("YES")
else:
    print("NO")
