# Hamiltonian and Lagrangian :--


def check(arr):
    temp = arr[0]
    for i in arr:
        if temp < i:
            return False
    return True

n = int(input())
m = list(map(int,input().split()))
m.append(0)
for i in range(n):
    if check(m[i:]):
        print(m[i],end=' ')

'''
def check(arr):
    temp = arr[0]
    for i in arr:
        if temp < i:
            return False
    return True

n = int(input())
m = list(map(int,input().split()))
arr = [m[0]]
for i in range(n):
    if check(m[i:]) or i==n-1:
        print(m[i],end=' ')
'''
