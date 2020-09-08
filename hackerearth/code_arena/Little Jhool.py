# Little Jhool
for _ in range(int(input())):
    a,b,m = map(int,input().split())
    hop = (b+1-a) // m
    print(hop)
