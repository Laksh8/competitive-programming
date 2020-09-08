# Nuclear Reactors :--

a ,n ,k = map(int,input().split())
lst = [0]*k
count = 0

for i in range(1,a+1):
    if i % n:
        lst[count] = 0
        count +=1
    lst[count] = i % n 
        
