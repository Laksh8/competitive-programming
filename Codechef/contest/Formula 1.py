# Formula 1 :--


for _ in range(int(input())):
    lst = []
    for __ in range(int(input())):
        name = input()
        val = int(input())
        lst.append([val,name])
    
    lst.sort()
    for i in lst:
        print(i[1])

