# Book of Potion making :

val = list(map(int,input()))

temp = 0
for i in range(1,len(val)+1):
    temp = temp + i*val[i-1]
if temp %11 == 0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")
