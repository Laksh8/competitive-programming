def selectEvenNumber(list1):
    lst = []
    for arg in list1:
        if arg % 2 ==0:
            lst.append(arg)

    return lst

lst = list(map(int,input("Enter All the Numbers :-- ").split()))
print(selectEvenNumber(lst))

