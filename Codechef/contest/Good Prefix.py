# Good Prefix :

for _ in range(int(input())):
    arr = []
    s = input()
    count = 0
    k,x = map(int,input().split())
    for i in range(len(s)):
        if s[i] not in arr :
            arr.append(s[i])
            count +=1
        elif k>0:
            k-=1
        else:
            break
    print(count)


'''
for _ in range(int(input())):
    arr = []
    s = input()
    count = 0
    k,x = map(int,input().split())
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
            count +=1
        else:
           break
    print(count)
'''
