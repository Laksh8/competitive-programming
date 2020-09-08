# Anagrams

for _ in range(int(input())):
    a = input()
    b = input()   
    lst = list(set(a)&set(b))
    count = len(a)+len(b)
    
    for i in range(len(lst)):
        count = count-(2*(min(a.count(lst[i]),b.count(lst[i]))))
    print(count)
