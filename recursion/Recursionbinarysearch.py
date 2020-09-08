def BinarySearch(start,end,lst,value):
    mid = (start+end)//2

    if lst[mid] == value:
        return mid

    elif lst[mid] > value:
        return BinarySearch(start,mid,lst,value)

    else:
        return BinarySearch(mid,end,lst,value)
    
lst = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(0,len(lst)-1,lst,7))
