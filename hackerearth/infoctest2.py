# Question 2


st = input()
n = len(st)
lst = []
for i in range(n): 
        for len in range(i+1,n+1): 
            if str(int(st[i: len]) * (int(st[i: len]) + 1)) in st:
                lst.append(int(st[i: len]))

lst = sorted(list(set(lst)))
            

if lst:
    print(str(lst)[1:-1])
else:
    print("-1")




'''
lst = []
for i in range(int(n)):
    if str(i * (i+1)) in n:
        lst.append(i)

'''

