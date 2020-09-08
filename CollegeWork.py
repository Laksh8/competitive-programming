# Work :--


def check(lstN,lstR):
    unused = []
    lstN.sort(reverse=True)
    su = sum(lstR)
    w = k =i= 0
    temp = lstN.copy()
    
    for i in range(len(lstN)):
        print(sum(lstN[:i]), su)
        if sum(lstN[:i+1]) >= su:
            print(lstN[:i+1])
            w = sum(lstN[:i+1]) - su
            unused.extend(lstN[i+1:])
            break
        
    return w,unused
            
'''
lstN = []
for _ in range(int(input())):
    l,b,h = map(int,input().split())
    lstN.append(2*(l*b + b*h + l*h))
lstN.sort()
lstR = []
for _ in range(int(input())):
    l,b,h = map(int,input().split())
    lstR.append(2*(l*b + b*h + l*h))

lstR.sort()

print(check(lstN,lstR))
'''
