# Little Deepu and Little Kuldeep :--
'''
for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    count = 1
    for i in range(1,n):
        if lst[i-1] == lst[i]:
            count +=1
    print(count)
'''


n = int(input())
lst = list(map(int,input().split()))

count = 0
for i in range(n-1):
    count += lst[i] * lst[i+1]

print(count%1000000007)
