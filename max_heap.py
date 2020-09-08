# Max Heap :

def insert(lst,data):
    lst.append(data)
    if lst[len(lst)//2-1] < data:
        lst[len(lst)//2-1] ,lst[len(lst)-1] = lst[len(lst)-1],lst[len(lst)//2-1]
        return insert(lst[:len(lst)//2-1],data)
    return lst

