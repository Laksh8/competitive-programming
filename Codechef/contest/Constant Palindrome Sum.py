# Constant Palindrome Sum :--

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(1,(n//2)):
        if a[i] != a[n-i] and a[n-i] <= k:
            count +=1
    print(count)
