# Solution Explanation

This solution is based on the dynamic programming approach, and I'd like to acknowledge the helpful explanation provided by the channel [Tushar Roy - Coding Made Simple](https://www.youtube.com/watch?v=8LusJS5-AGo&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=1).

## Example Scenario

Let's illustrate the solution with the following example:

  * Capacity = 7
  * Items: I1 (weight 1, value 1), I3 (weight 3, value 4), I4 (weight 4, value 5), I5 (weight 5, value 7)

## Dynamic Programming Table

The core idea is to build a table that represents the maximum achievable value for increasing capacity limits and item sets. The table's structure is as follows:

|      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **-** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **I1** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **I3** | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
| **I4** | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
| **I5** | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

  * **Columns:** Represent the knapsack's capacity, ranging from 0 to the target capacity (7 in this case).
  * **Rows:** Represent the available items. For example, the row for I4 considers the item set {I1, I3, I4}.
  * **Initialization:** The first row and column are filled with 0s. A capacity of 0 or no available items results in a maximum value of 0. The I1 row is also simple to fill because if there is capacity, we can take it, if not, we can't.

### Filling the Table

We fill the table row by row, building up the solution. For each cell `table[item][capacity]`, we consider two choices:

1.  **Don't include the current item:** The maximum value is the same as the maximum value achievable with the previous set of items (the row above) and the same capacity (`table[item-1][capacity]`).
2.  **Include the current item (if its weight <= current capacity):** The maximum value is the current item's value + the maximum value achievable with the previous set of items with the remaining capacity (`current item value + table[item-1][capacity - current item weight]`).

We choose the option that yields the higher value.

### Example Walkthrough

  * **Row I3:** For capacities less than 3, we can't fit I3, so we inherit the values from the I1 row. At capacity 3, we can include I3 (value 4) or exclude it (value 1 from the I1 row). We choose 4. For capacities >= 3, we can potentially include I3 along with I1.
  * **Row I4:** This is where the dynamic programming aspect shines. For capacity 6, if we *don't* include I4, the best value is 5 (from the I3 row, `table[I3][6]`). If we *do* include I4 (value 5), we have a remaining capacity of 2. The best value for capacity 2 with items {I1, I3} is 1 (from `table[I3][2]`). So, including I4 gives us a value of 5 + 1 = 6. We choose 6.
  * **Row I5:** Similar logic applies. For capacity 7, if we *don't* include I5, the best value is 9 (from the I4 row, `table[I4][7]`). If we *do* include I5 (value 7), we have a remaining capacity of 2. The best value for capacity 2 with items {I1, I3, I4} is 1 (from `table[I4][2]`). So, including I5 gives us a value of 7 + 1 = 8. We choose 9. The final value at `table[I5][7]` is 9.

### Benefits of Dynamic Programming

Instead of checking all 2<sup>N</sup> combinations of items (where N is the number of items), we efficiently build up the solution by reusing previously calculated optimal values for smaller subproblems.

## Backtracking to Find Selected Items

Once the dynamic programming table is fully populated, we can reconstruct the set of items that yield the maximum value by "backtracking" from the final optimal cell.

Let's use the completed table from our example:

|      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **-** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **I1** | <span style="color:green;">0</span> | 1 | 1 | <span style="color:red;">1</span> | 1 | 1 | 1 | 1 |
| **I3** | 0 | 1 | 1 | <span style="color:green;">4</span> | 5 | 5 | 5 | <span style="color:red;">5</span> |
| **I4** | 0 | 1 | 1 | 4 | 5 | 6 | 6 | <span style="color:green;">9</span> |
| **I5** | 0 | 1 | 1 | 4 | 5 | 7 | 8 | <span style="color:green;">9</span> |

We start at the cell representing the final optimal solution: `table[I5][7]` (value 9). We then move backward, deciding at each step whether the current item (the item corresponding to the current row) was included or not.

1.  **Current: `table[I5][7]` (Value 9)**

      * Compare `table[I5][7]` (9) with `table[I4][7]` (9).
      * Since these values are *equal*, it means the optimal value of 9 at capacity 7 was achieved *without* including Item I5.
      * We move up to the previous row: `table[I4][7]`.

2.  **Current: `table[I4][7]` (Value 9)**

      * Compare `table[I4][7]` (9) with `table[I3][7]` (5).
      * Since `table[I4][7]` (9) is *greater* than `table[I3][7]` (5), it indicates that Item I4 *was* included to achieve this value.
      * Add **I4** to our selected items.
      * Reduce the remaining capacity by I4's weight (7 - 4 = 3).
      * Move diagonally up to `table[I3][3]`.

3.  **Current: `table[I3][3]` (Value 4)**

      * Compare `table[I3][3]` (4) with `table[I1][3]` (1). (Note: I2 would be a placeholder for the item *before* I3, which is I1. If your table directly uses item indices, it would be `table[i-1][w]`).
      * Since `table[I3][3]` (4) is *greater* than `table[I1][3]` (1), it indicates that Item I3 *was* included.
      * Add **I3** to our selected items.
      * Reduce the remaining capacity by I3's weight (3 - 3 = 0).
      * Move diagonally up to `table[I1][0]`.

4.  **Current: `table[I1][0]` (Value 0)**

      * Our remaining capacity is now 0. This means we have found all items that contribute to the maximum value.

Therefore, the final set of items that produces the maximum value of 9 is **{I4, I3}**. This process demonstrates how we can efficiently trace back through the DP table to reconstruct the specific choices made.