# Aman & Mr.Sharma :
count = 0
for _ in range(int(input())):
    r,x = map(int,input().split())
    p = (2*r*22)/7
    if p<x*100:
        count+=1
print(count)
