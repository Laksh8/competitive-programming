def partition(arr,low,high):
    i,pivot = low , arr[high]

    for j in range(low,high):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[high] = arr[high],arr[i]
    return i

def QuickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)        
            
    
lst = [10, 7, 8, 9, 1, 5] 
n = len(lst) 
QuickSort(lst,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %lst[i])
