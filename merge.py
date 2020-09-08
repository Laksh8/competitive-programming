'''
def MergeArray(arr1,arr2):
    i = j = k =0
    arr3 = [None] * (len(arr1)+len(arr2))

    while i<len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i,k =i+1,k+1
        else:
            arr3[k] = arr2[j]
            j,k =j+1,k+1

    while i < len(arr1): 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1
  
    # Store remaining elements  
    # of second array 
    while j < len(arr2): 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1

    return arr3
'''
def MergeArray(arr1, arr2, n1, n2): 
    arr3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
  
    # Traverse both array 
    while i < n1 and j < n2: 
      
        # Check if current element  
        # of first array is smaller  
        # than current element of  
        # second array. If yes,  
        # store first array element  
        # and increment first array 
        # index. Otherwise do same  
        # with second array 
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else: 
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1
      
  
    # Store remaining elements 
    # of first array 
    while i < n1: 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1
  
    # Store remaining elements  
    # of second array 
    while j < n2: 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1
    return arr3

    
