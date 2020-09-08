# Chef and Numbers :--

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    lst = [arr[0]]
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            lst.append(arr[i])
    x = sorted(list(set(lst)),reverse=True)
    temp = 0
    for i in x:
        if lst.count(i) > temp:
            temp = i
    print(temp)
    
        
