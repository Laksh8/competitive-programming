# Lift Requests :--


for _ in range(int(input())):
    n,q = map(int,input().strip().split())
    ini = temp = 0
    for i in range(q):
        fi , di = map(int,input().split())
        if temp != fi:
            ini += abs(fi-temp)
            ini += abs(fi-di)
            temp = di
        else:
            ini += abs(fi-di)
            temp = di
    print(ini)
