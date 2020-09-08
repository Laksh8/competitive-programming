import numpy as np

def dfs(arr,v)


# Bishu and his Girlfriend :
n = int(input())
arr = np.zeros([n,n],dtype= np.int0)
for i in range(n-1):
    u,v = map(int,input().split())
    arr[u-1][v-1] = 1
q = []
for _ in range(int(input())):
    q.append(int(input()))

