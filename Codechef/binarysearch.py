# Binary Search :--
def search(start,end,arr,value):
    mid = (start+end)//2

    while start <= end:
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return search(start,mid,arr,value)

        else:
            return search(mid,end,arr,value)

lst = [1,2,3,4,5,6,7,8,9]

print(search(0,len(lst)-1,lst,2))

            
                
