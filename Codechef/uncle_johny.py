# Uncle Johny :--

def uncle(n,song,k):
    a = song[k-1]
    song.sort()
    print(song.index(a)+1)


t = int(input())
for i in range(t):
    n = int(input())
    song = list(map(int,input().split()))
    k = int(input())
    uncle(n,song,k)

'''def uncle(n,song,k):
    a = song[k-1]
    song = mergesort(song)
    return search(0,len(song),song,a)+1

def mergesort(arr):
    if len(arr) > 1: 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]


        mergesort(left)
        mergesort(right)


        i =j =k =0
        while i<len(left) and j < len(left):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k +=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr

def search(start,end,arr,value):
    mid = (start+end)//2

    while start <= end:
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return search(start,mid,arr,value)

        else:
            return search(mid,end,arr,value)

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    k = int(input())
    print(uncle(n,lst,k))
'''

