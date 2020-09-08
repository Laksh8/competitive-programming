# IT’S MAGIC!


n = int(input())
lst = list(map(int,input().split()))
val = max(lst)
x = sum(lst)
y = True
for i in range(n):
    if x%7==0 and lst[i]%2 == 0 and val>lst[i]:
        val=lst[i]
        index = i
        print(index)
        y = False
    elif lst[i]==x%7:
        index = i;print(index);break
if y:
    print(-1)
else:
    print(index)
