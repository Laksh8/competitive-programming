# Your friend Tanya
for _ in range(int(input())):
    l = int(input())
    lst = list(map(int,input().split()))
    count = 0
    for i in range(l):
        lst[i] = [lst[i],i+1]
    lst.sort()
    for i in lst:
        if i[1] <= l:
            l-=i[1]
            count += i[0]
    print(count)
