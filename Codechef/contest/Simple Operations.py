# Simple Operations :--

for _ in range(int(input())):
    s1 = list(map(str,input()))
    s2 = list(map(str,input()))
    count =  0
    a = b = 1 
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count +=2
    print(count )
