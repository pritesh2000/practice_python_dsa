num = 5
minRow = 0 
minCol = 0
maxRow = num -1
maxCol = num -1

import pandas as pd
import numpy as np

matr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(matr)
i = 1

for j in range(num):
    for k in range(num):
        print(matr[j][k],end=" ")
    print()