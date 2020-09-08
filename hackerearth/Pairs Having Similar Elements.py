n  = int(input())
lst = list(map(int,input().split()))
lst.sort()
j = k = 0
count = 0
for index,value in enumerate(lst):
    j = index + 1
    k = index + 2
    try:
        if lst[j] == value+1:
            count +=1
            print('(',value,',',lst[j],")")
            if lst[k] == value+2:
                count+=2
                print('(',value,',',lst[k],")")
        if lst[k] == value+1:
            count +=1
            print('(',value,',',lst[k],")")
        
    except IndexError:
        pass

print(count)
