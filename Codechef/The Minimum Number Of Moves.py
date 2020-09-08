# The Minimum Number Of Moves :

for _ in range(int(input())):
    n = int(input())
    s = list(map(str,input()))
    temp = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
        elif temp<count:
            temp = count

    print(count)  

'''
for _ in range(int(input())):
    n = int(input())
    w = list(map(int,input()))
    while True:
        x = max(w)
        if w.count(x) == len(w):
            print(count)
            break
'''
