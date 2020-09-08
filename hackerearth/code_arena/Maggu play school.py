# Maggu play school :--
for _ in range(int(input())):
    s = input()
    lst = ['A',"a","B","b","C","c"]
    count = 0
    temp = 0
    i = 0
    while i<len(s):
        temp = 0
        if s[i] in lst:
            while i<len(s) and s[i] in lst:
                temp +=1
                i+=1
            count = temp *(temp+1)/2
        print(count,end="this is for fun")
        i+=1
    if str(count).split(".")[-1] != '0':
        count +=1


    print(str(count).split(".")[-1] , end="asdgasd")
    print(int(count))


