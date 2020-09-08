# New balanced Bracker :--

s = input()
v1= v2= v= 0
for i in s:
    if i == '{':
        print(v1)
        v1+=1
    else:
        print(v2)
        v2 +=1

if v2 == 2*v1:
    print(v)
elif v2 > 2*v1:
    v = v2-(2*v1)
    print(v*2)
else:
    v = (v1*2)-v2

print(v)
'''

def solve (s):
    v1 = v2 = v = 0
    for i in s:
        if i == '{':
            v1 +=1
        else:
            v2 +=1
    
    if v2 == v1*2:
        return v
    elif v2 > 2*v1:
        return (v2 - (2*v1))*2
    else:
        return v1*2 - v2
        

    
T = int(input())
for _ in range(T):
    S = input()

    out_ = solve(S)
    print (out_)
'''
