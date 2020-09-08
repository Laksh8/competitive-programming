
def MergeSort(lst):
    if len(lst) >1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]

        MergeSort(L)
        MergeSort(R)
        
        i = j = k =0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i +=1
            else:
                lst[k] = R[j]
                j +=1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            lst[k] = R[j]
            j+=1
            k+=1
        
    return lst

a = [5,6,7,8,9,0,7,6,5,4,3,1]

print(MergeSort(a))

    
