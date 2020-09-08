# Seven-Segment Display :

dic = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}


for _ in range(int(input())):
    val = input()
    n = 0
    for i in val:
        n += dic[int(i)]
        
    if n % 2 == 0:
        temp = ""
        for i in range(n//2):
            temp +='1'
    else:
        temp = ""
        for i in range((n//2)-1):
            temp+='1'
        temp = '7' + temp
    print(temp)

'''
for _ in range(int(input())):
    n = dic[int(input())]
    if n % 2 == 0:
        temp = ""
        for i in range(n//2):
            temp +='1'
    else:
        temp = ""
        for i in range((n//2)-1):
            temp+=1
        temp+='7'
    print(temp)
'''
