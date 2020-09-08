# Coin Flip
def coinflip(i,n,q):
	if n%2==0:
		return n//2
	else:
		if i==q:
			return n//2
		else:
			return n//2+1
t=int(input())
for i in range(t):
	g=int(input())
	for j in range(g):
		i,n,q=map(int,input().split())
		print(coinflip(i,n,q))

'''
def coinflip(i,n,q):
    lst = []
    if n %2 == 0:
            lst.append(i)
    else:
        if i ==1:
            lst.append(2)
        else:
            lst.append(1)
    for i in range(n-1):
        if lst[-1] == 1:
            lst.append(2)
        else:
            lst.append(1)
    count = 0    
    for i in lst:
        if i ==q:
            count+=1
    return count

t = int(input())
dic = {1:2,2:1}
for i in range(t):
    g = int(input())
    for i in range(g):
        i,n,q = map(int,input().split())
        lst = []
        if n %2 == 0:
                lst.append(i)
        else:
            lst.append(dic[i])
            
        for j in range(n-1):
            lst.append(dic[lst[-1]])


        count = 0    
        for j in lst:
            if j ==q:
                count+=1
        print(count)
'''
