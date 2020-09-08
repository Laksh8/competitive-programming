
lst = list(map(int,input("Enter Values :-- ").split()))
value = int(input("Enter Element You want to search :-- "))

first = 0
last = len(lst)
middle = first+last//2

while(True):
    if value == lst[middle]:
        print("\n\n",middle)
        break
    elif(first==value):
        print(first)
        break
    elif(last==value):
        print(last)
        break
    elif value < lst[middle]: 
        last = middle-1
        print(first,last)
    
    elif value > middle:
        first = middle+1
        print(first,last)
    if first == last:
        print("Not Found")
        break
    middle = first+last//2
