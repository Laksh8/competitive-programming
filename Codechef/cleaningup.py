# Cleaning Up :--

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    lst = list(range(1,n+1))
    lst1 =  list(map(int,input().split()))
    for i in lst1:
        lst.remove(i)

    chef = []
    ass = []
    for index, element in enumerate(lst):
        if index %2 !=0:
            ass.append(element)
        else:
            chef.append(element)

    for i in chef:
        print(i,end=' ')
    print()

    for i in ass:
        print(i,end=' ')
    print()
