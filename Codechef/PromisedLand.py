import numpy as np

t = int(input("Enter Test Cases :-- "))

n,m = map(int,input("Enter Vertical , Horizontal Values:-- ").split())

x,y,s = map(int,input("Enter Number of riveres in vertical,horizontal , Dimantion of House :-- ").split())

arr = np.zeros((n,m),dtype=np.int32)

xi = list(map(int,input("Enter Coordinates of River flowing through x axis :-- ").split()))

yi = list(map(int,input("Enter Coordinates of River flowing through y axis :-- ").split()))

def home(s,i,arr):
    
        

for i in xi:
    arr[i-1] = 1

for i in yi:
    for j in range(n):
        for k in range(m):
            arr[j][i-1] = 1



