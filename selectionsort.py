#Selection Sort :--

def SelectionSort(arr):
    '''
    for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        A[i], A[min_idx] = A[min_idx], A[i] 
    '''
    index = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[index],arr[i] = arr[i],arr[index]

    return arr

lst = list(map(int,"5,6,7,8,9,0,7,6,5,4,3,1".split(",")))
print(lst)
print(SelectionSort(lst))

        
