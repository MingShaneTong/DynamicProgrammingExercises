from typing import List
from helper import Item

def solution(capacity: int, items: List[Item]) -> List[Item]:
    sorted_items: List[Item] = sorted(items, key=lambda item: item.weight)
    optimal_table = populate_optimal_value_table(capacity, sorted_items)
    return backtrace_items(capacity, sorted_items, optimal_table)

def populate_optimal_value_table(capacity: int, sorted_items: List[Item]) -> List[List[int]]:
    optimal_values_table = [[0 for c in range(capacity + 1)]]
    # add each item into the pool of items to add
    for item in sorted_items:
        item_optimal_table = [0]
        # find the maximum value at the new capacity given items
        for c in range(1, capacity + 1):
            optimal_without_item = optimal_values_table[-1][c]
            optimal_with_item = item.value + optimal_values_table[-1][c - item.weight] if item.weight <= c else optimal_without_item
            optimal_value = max(optimal_without_item, optimal_with_item)
            item_optimal_table.append(optimal_value)

        optimal_values_table.append(item_optimal_table)
    
    return optimal_values_table

def backtrace_items(capacity: int, sorted_items: List[Item], optimal_table: List[List[int]]) -> List[Item]:
    pointer_capacity = capacity
    pointer_row = len(sorted_items)
    items_included = []

    while pointer_capacity > 0 and pointer_row > 0:
        # if the value is better with the item, then add to knapsack
        if optimal_table[pointer_row][pointer_capacity] != optimal_table[pointer_row - 1][pointer_capacity]:
            item = sorted_items[pointer_row - 1]
            items_included.append(item)
            pointer_capacity -= item.weight
        pointer_row -= 1
    
    return items_included
