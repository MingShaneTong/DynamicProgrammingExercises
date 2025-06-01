import numpy as np
from numpy.typing import ArrayLike

def solution(str1: str, str2: str) -> int:
    med_table = populate_med_table(str1, str2)
    return med_table[-1][-1]

def populate_med_table(str1: str, str2: str) -> ArrayLike:
    med_table = np.zeros((len(str1) + 1, len(str2) + 1))
    med_table[:, 0] = range(len(str1) + 1)
    med_table[0] = range(len(str2) + 1)

    for i1 in range(1, len(str1) + 1):
        for i2 in range(1, len(str2) + 1):
            if str1[i1 - 1] == str2[i2 - 1]:
                med_table[i1][i2] = med_table[i1 - 1][i2 - 1]
            else: 
                med_table[i1][i2] = min(
                    med_table[i1 - 1][i2], 
                    med_table[i1][i2 - 1],
                    med_table[i1 - 1][i2 - 1]
                ) + 1
    
    return med_table
