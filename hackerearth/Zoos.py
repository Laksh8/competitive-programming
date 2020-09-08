# Zoos

value = input()
x =y =0

for i in value:
    if i == 'z':
        x+=1
    else:
        y+=1
if x*2==y and x!=0 and y!=0:
    print("Yes")
else:
    print("No")
