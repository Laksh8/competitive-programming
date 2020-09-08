# Fractional Knapsack Problem :--

# Formating is (Value , Weight)
values = list(map(int,input("Enter all the Values :-- ").split()))
weights = list(map(int,input("Enter all the Weights :-- ").split()))

lst = []
for value,weight in zip(values,weights):
    lst.append((value,weight,value/weight))

lst.sort(key=lambda x:x[2])

maximum = int(input("Enter Maximum Weight :-- "))

profit = w = 0


for value,weight,x in lst:

    if maximum - weight > 0:
        profit += value
        w += weight   
        maximum -= weight

    else:
        profit += (maximum/weight)*value
        maximum = 0
        


    
