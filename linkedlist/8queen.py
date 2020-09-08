import numpy as np

n = int(input("Enter Number of Queens :-- "))

array = np.ones([n,n],dtype=np.str_)


for i in range(len(array)):
    for j in range(len(array)):
        if(i==0 and j == len(array)//2):
            for k in range(len(array)//2):
                array[i][j] = "Q"
                i +=1
                j +=2
        if(i==len(array)-1 and j == len(array)//2+1):
            for k in range(len(array)//2-1):
                array[i][j] = "Q"
                j -=2
                i -=1
                

print(array)
    
