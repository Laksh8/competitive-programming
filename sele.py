# Selection Sort :--

def SelectionSort(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i]> lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

lst = list(map(int,input().split()))

print(str(SelectionSort(lst))[1:-1])
