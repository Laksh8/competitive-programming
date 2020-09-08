# Not All Flavours



for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    lst = set([x for x in range(1,k+1)])

    le = 0
    for i in range(len(a)):
        for j in range(len(a)):
            val = a[i:j+1]
            if set(val) != set(lst):
                  if le < len(val):
                      le = len(val)
    print(le)

