# Best Index....

n = int(input())
arr = list(map(int,input().split()))
su = 0
for i in range(n):
    
    if i < n-3:
        print(arr[i:i+3])
        if su <sum(arr[i:i+3]):
            
            su = sum(arr[i:i+3])
    elif i> n-3:
        if su < sum(arr[i:]):
            print(arr[i:])
            su = sum(arr[i:])
print(su)
