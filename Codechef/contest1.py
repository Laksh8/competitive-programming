# Under the Tunnels :--

4












# Bob and His Friends
'''
def closest(lst, K): 
        return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

t = int(input())

for i in range(t):
    n,a,b,c = map(int,input().split())
    f = list(map(int,input().split()))
    neara = closest(f,a)
    nearb = closest(f,b)
    if neara>nearb:        
        if nearb-b < 0:
            time = b-nearb+c
        else:
            time = nearb-b+c

        if nearb-a < 0:
            time += a-nearb
        else:
            time += nearb-a

    else:
        if neara-b < 0:
            time = b-nearb+c
        else:
            time = neara-b+c

        if nearb-a < 0:
            time += a-neara
        else:
            time += neara-a

    print(time)
'''
    










# Chef and Street Food
'''
t = int(input())

for i in range(t):
    n = int(input())
    profit = 0
    for i in range(n):
        si,pi,vi = map(int,input().split())
        if pi % si !=0:
            r = pi%si
            print(r)
            if profit < (r*vi):
                profit = r*vi
print(profit)
'''
