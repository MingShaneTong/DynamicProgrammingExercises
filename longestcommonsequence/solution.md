# Solution Explanation

This solution is based on the dynamic programming approach, and I'd like to acknowledge the helpful explanation provided by the channel [Tushar Roy - Coding Made Simple](https://www.youtube.com/watch?v=NnD96abizww&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2).

## Example Scenario

Let's illustrate the solution with the following example:

* **String 1 (str1):** `"abcdaf"`
* **String 2 (str2):** `"acbcf"`

## Dynamic Programming Table

The core idea is to build a table that represents the maximum lcs length value for each increasing substring. The table's structure is as follows:

|      | _ | a | b | c | d | a | f |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **-** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **a** | 0 |   |   |   |   |   |   |
| **c** | 0 |   |   |   |   |   |   |
| **b** | 0 |   |   |   |   |   |   |
| **c** | 0 |   |   |   |   |   |   |
| **f** | 0 |   |   |   |   |   |   |

  * **Columns:** Represent the substring in str1 up to that letter.
  * **Rows:** Represent the substring in str2 up to that letter.
  * **Initialization:** The first row and column are filled with 0s. If there is no string to search then the lcs is automatically 0. 

### Filling the Table

We fill the table row by row which means we are comparing substrings of each of the given strings to inform the lcs of the larger substring, building up the solution. For each cell `table[i][j]`, we consider two choices:

If str2[i] == str1[j]: The characters match. The LCS length is 1 + the LCS length of the prefixes without these characters: table[i][j] = 1 + table[i-1][j-1].
If str2[i] != str1[j]: The characters don't match. The LCS length is the maximum of the LCS lengths we could get by excluding either str2[i] or str1[j]: table[i][j] = max(table[i-1][j], table[i][j-1]).

### Example Walkthrough

* **`table[a][a]`:** `str2[0]` ('a') == `str1[0]` ('a').  `table[a][a]` = 1 + `table[-][-]` = 1 + 0 = 1.
* **`table[a][b]`:** `str2[0]` ('a') != `str1[1]` ('b').  `table[a][b]` = max(`table[-][b]`, `table[a][a]`) = max(0, 1) = 1.
* **`table[a][c]`:** `str2[0]` ('a') != `str1[2]` ('c'). `table[a][c]` = max(`table[-][c]`, `table[a][b]`) = max(0, 1) = 1.
* ... (The 'a' row remains 1 until the end, as 'a' is present in str1)
* **`table[c][a]`:** `str2[1]` ('c') != `str1[0]` ('a'). `table[c][a]` = max(`table[a][a]`, `table[c][-]`)= max(1, 0) = 1.
* **`table[c][b]`:** `str2[1]` ('c') != `str1[1]` ('b'). `table[c][b]` = max(`table[a][b]`, `table[c][a]`) = max(1, 1) = 1.
* **`table[c][c]`:** `str2[1]` ('c') == `str1[2]` ('c'). `table[c][c]` = 1 + `table[a][b]` = 1 + 1 = 2.
* ...
* **`table[b][b]`:** `str2[2]` ('b') == `str1[1]` ('b'). `table[b][b]` = 1 + `table[c][a]` = 1 + 1 = 2.
* ...
* **`table[c][c]`:** `str2[3]` ('c') == `str1[2]` ('c'). `table[c][c]` = 1 + `table[b][b]` = 1 + 2 = 3.
* ...
* **`table[f][f]`:** `str2[4]` ('f') == `str1[5]` ('f'). `table[f][f]` = 1 + `table[c][a]` = 1 + 3 = 4.

* And so on, filling the table. The final value, `table[f][f]` = 4, represents the length of the LCS.

### Benefits of Dynamic Programming

Instead of finding all combinations of substrings of str1 and checking if it exists in str2, we gradually increase the size of the substring and use the data we obtained from the smaller substrings to calculate the longest lcs for the bigger string.

## Backtracking to Find LCS

Let's use the completed table from our example:

|      | _ | a | b | c | d | a | f |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **-** | <span style="color:green;">0</span> | 0 | 0 | 0 | 0 | 0 | 0 |
| **a** | 0 | <span style="color:green;">1</span> | 1 | 1 | 1 | 1 | 1 |
| **c** | 0 | <span style="color:green;">1</span> | 1 | 2 | 2 | 2 | 2 |
| **b** | 0 | 1 | <span style="color:green;">2</span> | 2 | 2 | 2 | 2 |
| **c** | 0 | 1 | 2 | <span style="color:green;">3</span> | <span style="color:green;">3</span> | <span style="color:green;">3</span> | 3 |
| **f** | 0 | 1 | 2 | 3 | 3 | 3 | <span style="color:green;">4</span> |

We start at the last cell: `table[f][f]` (length 4). We then move backward, deciding at each step whether the current item (the item corresponding to the current row) was included or not.

1.  **Current: `table[f][f]` (Length 4)**

      * Compare the length on top (length 3) and left (length 3) of the cell.
      * Since these values are *not equal* to `table[f][f]`, it means the lcs was constructed with the character f. 
      * We move diagonally to `table[c][a]`.

2.  **Current: `table[c][a]` (Length 3)**

      * Compare the length on top (length 2) and left (length 3) of the cell.
      * Since the left value is *equal* to `table[c][a]`, it means the lcs was found of similar length was found with a smaller substring of str1.
      * We move horizontally to `table[c][d]`.

3.  **Current: `table[c][d]` (Value 3)**

      * Left value the same as current value. Move to `table[c][c]`

4.  **Current: `table[c][c]` (Value 3)**

      * Top (length 2) and left (length 2) of the cell does not have the same value as `table[c][c]`, it means the lcs was constructed with the character c.
      * We move diagonally to `table[b][b]`.

If we continue this process until we reach the edges of the table, we find that the characters used were `f, c, b, a` which we reverse to get `abcf`.