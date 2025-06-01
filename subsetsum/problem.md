# Subset Sum Problem

## Problem Description

The **Subset Sum Problem** is a classic problem in computer science, particularly in the realm of combinatorial optimization. Given a set of non-negative integers and a target sum, the problem asks whether there exists a subset of the given set whose elements sum up to the target sum.

**Key characteristics:**
* We are looking for a *boolean* answer: `True` if such a subset exists, `False` otherwise.
* Each element from the given set can be used at most once (it's either included in the subset or not).

This problem is known to be NP-complete, but it can be solved efficiently using dynamic programming for cases where the target sum and the number of elements are within reasonable bounds.

## Example

Let's illustrate the problem with an example:

**Given:**
* `set = {3, 34, 4, 12, 5, 2}`
* `target_sum = 9`

**Does a subset exist that sums to 9?**

Let's check:
* `{3, 4, 2}` sums to $3 + 4 + 2 = 9$.
* `{4, 5}` sums to $4 + 5 = 9$.

Since at least one such subset exists, the answer is **`True`**.

**Another Example:**

* `set = {3, 34, 4, 12, 5, 2}`
* `target_sum = 10`

In this case, no combination of the numbers in the set sums exactly to 10. So, the answer would be **`False`**.
