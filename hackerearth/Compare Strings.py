# Compare Strings
n,q = map(int,input().split())
a = input()
b = input()
count = 0
for _ in range(q):
    if b[int(input())-1] != '1':
        count +=1
    
    if a.count('1') > b.count('1')+count :
        print("NO")
    else:
        print("YES")
