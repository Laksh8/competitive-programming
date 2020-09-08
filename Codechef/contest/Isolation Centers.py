# Isolation Centers :--

for _ in range(int(input())):
    n,q = map(int,input().split())
    s = input()
    x = list(set(map(str,s)))
    for __ in range(q):
        c = int(input())
        count = 0
        for i in x:
            if s.count(i) >= c:
                count += s.count(i)-c
        print(count)
