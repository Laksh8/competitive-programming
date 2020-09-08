# sequence of non-negative :
n = int(input())
a = list(map(int,input().split()))
'''
if a.count(a[0]) == len(a):
    print("YES")
else:
    print("NO")

'''
while(0 not in a):
    for i in range(n-1):
        a[i]-=1
        a[i+1]-=1

if a.count(0) == len(a):
    print("YES")
else:
    print("NO")
