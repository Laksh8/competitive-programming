# Lonely Monk :

n = int(input())

a = list(map(int,input().split()))

i = temp = count = 0
while i < n:
    if a[i] %2 != 0 :
        x = i - temp
        count += (x*(x+1)) //2
        temp = i+1
    i+=1
if i != temp:
    x = i - temp
    count += (x*(x+1)) //2

print(count)

        
