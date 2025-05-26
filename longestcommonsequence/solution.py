import numpy as np
from numpy.typing import ArrayLike

def solution(str1: str, str2: str) -> str:
    lcs_table = populate_lcs_table(str1, str2)
    return find_lcs(str1, str2, lcs_table)

def populate_lcs_table(str1: str, str2: str) -> ArrayLike:
    lcs_table = np.zeros((len(str1) + 1, len(str2) + 1))

    for i1 in range(1, len(str1) + 1):
        for i2 in range(1, len(str2) + 1):
            if str1[i1 - 1] == str2[i2 - 1]:
                lcs_table[i1][i2] = lcs_table[i1 - 1][i2 - 1] + 1
            else: 
                lcs_table[i1][i2] = max(lcs_table[i1 - 1][i2], lcs_table[i1][i2 - 1])
    
    return lcs_table

def find_lcs(str1: str, str2: str, lcs_table: ArrayLike) -> str:
    p1 = len(str1)
    p2 = len(str2)
    lcs_reverse = ""

    while p1 > 0 and p2 > 0:
        if lcs_table[p1][p2] == lcs_table[p1 - 1][p2]:
            p1 -= 1
        elif lcs_table[p1][p2] == lcs_table[p1][p2 - 1]:
            p2 -= 1
        else:
            lcs_reverse += str1[p1 - 1]
            p1 -= 1
            p2 -= 1
    
    return ''.join(reversed(lcs_reverse))
