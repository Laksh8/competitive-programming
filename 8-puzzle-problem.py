import numpy as np

# 8-Puzzel Problem :

goal = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,None]])

start = np.array(
    [[5,4,8],
    [None,3,7],
    [1,6,2]])

def validmove(start,move):
    if move == 'U':
        if None in start[0]:
            return False
        else:
            return True
    
                
