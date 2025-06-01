import numpy as np
from numpy.typing import ArrayLike
from typing import List

def solution(target: int, number_list: List[int]) -> List[int]:
    sorted_number_list: List[int] = sorted([n for n in number_list if n <= target])
    if len(sorted_number_list) == 0:
        return []
    subset_sum_table = populate_subset_sum_table(target, sorted_number_list)
    solution_list = backtrace_subset(target, sorted_number_list, subset_sum_table)
    return solution_list

def populate_subset_sum_table(target: int, number_list: List[int]) -> ArrayLike:
    subset_sum_table = np.zeros((len(number_list), target + 1)).astype(bool)
    # empty subset always can achieve target of 0
    subset_sum_table[:, 0] = [True for i in range(len(number_list))]    
    # with only the first item, the set either contains that item or not
    subset_sum_table[0][number_list[0]] = True

    for i in range(1, len(number_list)):
        number = number_list[i]

        for c in range(1, target + 1):
            if subset_sum_table[i - 1][c] == True:
                subset_sum_table[i][c] = True
            elif c >= number:
                subset_sum_table[i][c] = subset_sum_table[i - 1][c - number]
    
    return subset_sum_table

def backtrace_subset(target: int, number_list: List[int], subset_sum_table: ArrayLike) -> List[int]:
    if subset_sum_table[-1][-1] == False:
        return []
    
    row = len(number_list) - 1
    col = target
    items_included = []

    while row >= 0 and col > 0:
        if row == 0 or subset_sum_table[row - 1][col] == False:
            items_included.append(number_list[row])
            col -= number_list[row]
        row -= 1
    return sorted(items_included)


target = 9
number_set = [3, 34, 4, 12, 5, 2]
expected = [2, 3, 4]
observed = solution(target, number_set)
print(observed)
