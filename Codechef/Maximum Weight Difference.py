# Maximum Weight Difference :--
for _ in range(int(input())):
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    child = chef = 0
    child = sum(w[:k])
    chef = sum(w[k:])
    print(chef-child)



'''
for _ in range(int(input())):
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    child = chef = 0
    for i in range(n):
        if i<k:
            child+=w[i]
        else:
            chef+=w[i]
    print(chef-child)
'''
