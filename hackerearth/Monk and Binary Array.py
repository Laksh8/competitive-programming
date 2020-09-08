# Monk and Binary Array

def solution(n,lst):
    count = 0
    for i in range(n):
        for j in range(i,n):
            if 1 in lst[i:j+1]:
                count+=1
        #for k in range(i,1+j):
         #   print(arr[k],end=" ")
        
    return count-1


n = int(input())
arr = list(map(int,input().split()))

val = 0
for _ in range(n):
    lst = arr.copy()
    if lst[_] == 0:
        lst[_] = 1
        c = solution(n,arr)
        if val < c:
            val = c

print(val)
