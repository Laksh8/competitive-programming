# Life, the Universe, and Everything
'''
while True:
    x = int(input())
    if x == 42:
        break
    else:
        print(x)
'''

t = int(input())

for i in range(t):
    index ,n = map(int,input().split())
    lst = list(range(0,3))
    temp = index
    for j in range(n):
        x = (temp+1) % len(lst)
        temp , lst[x] = lst[x] , temp
    print(temp)
