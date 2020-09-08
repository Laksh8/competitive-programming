import numpy as np

value = np.array([60,100,120],dtype=np.int32)
weight = np.array([10,20,30],dtype=np.int32)

max_k = 50

profite = 0
ratios = value/weight
for ratio in range(len(ratios)):
    if max_k>weight[ratio]:
        max_k = max_k-weight[ratio]
        profite = profite+value[ratio]
    else:
        profite = profite + max_k*ratios[ratio]
print(profite)
    
