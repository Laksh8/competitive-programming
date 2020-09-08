p = [(i, j)[::k] for i in (1, -1) for j in (2, -2) for k in (-1, 1)]
i, j, n = map(int, input().split())
d = {(i, j)}
for _ in range(n):
    t = set()
    for i, j in d:
        for dx, dy in p:
            x, y = i + dx, j + dy
            if 10 >= x >= 1 <= y <= 10:
                t.add((x, y))
    d = t
print(len(d))

'''
import numpy as np

# A Tryst With Chess :
global arr;arr = np.zeros( [10,10],np.int0)

def validmove(i,j,n,val):
    # Right-Up
    if i-1 >= 0 and j +2 < 10:
        arr[i-1][j+2] = 1
        if val < n:
            return validmove(i-1,j+2,n,val+1)
        
    # Left-Up
    if i-1 >= 0 and j -2 >=0:
        arr[i-1][j-2] = 1
        if val < n:
            return validmove(i-1,j-2,n,val+1)
            
    # Up - Right 
    if i-2 >= 0 and j+1 < 10:
        arr[i-2][j+1] = 1
        if val < n:
            return validmove(i-2,j+1,n,val+1)

    # Up - left
    if i-2>=0 and j-1<10:
        arr[i-2][j-1] = 1
        if val < n:
            return validmove(i-2,j-1,n,val+1)    
    # Right-down
    if i+1 < 10 and j +2 < 10:
        arr[i+1][j+2] = 1
        if val < n:
            return validmove(i+1,j+2,n,val+1)
        
    # Left-Up
    if i+1 < 10 and j -2 >=0:
        arr[i+1][j-2] = 1
        if val < n:
            return validmove(i+1,j-2,n,val+1)
        
    # Up - Right 
    if i+2 < 10 and j+1 < 10:
        arr[i+2][j+1] = 1
        if val < n:
            return validmove(i+2,j+1,n,val+1)
    # Up - left
    if i+2<10 and j-1<10:
        arr[i+2][j-1] = 1
        if val < n:
            return validmove(i+2,j-1,n,val+1)

    if val > n: 
        return True



i,j,n = map(int,input().split())
arr[i-1][j-1] = 1
count =  0
validmove(i-1,j-1,n,1)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            count +=1
print(count-1)
'''
