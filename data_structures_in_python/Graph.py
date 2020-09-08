import numpy as np
class Graph:
    def __init__(self,v,e):
        self.v = v
        self.e = e
        self.adj = np.zeros( [self.v,self.v] )


    def takedata(self):
        i , j = map(int,input("Enter Coordinate of the edge :-- ").split(','))
        self.adj[i][j] = 1

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                if self.adj[i][j] == 1:
                    print(f"Edge is : {i} , {j}")


obj = Graph(5,6)
for i in range(obj.e):
    obj.takedata()

print(obj.adj)


