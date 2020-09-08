# Bubble Sort :--

def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
    return lst

lst = list(map(int,input().split()))
print(BubbleSort(lst))
