# Longest Common Subsequence (LCS) Problem

## Problem Statement

The **Longest Common Subsequence (LCS)** problem aims to find the longest sequence of characters that appears in two given strings, in the same relative order, but not necessarily connected.

## Example

Let's use an example:

* **String 1 (str1):** `"abcdaf"`
* **String 2 (str2):** `"acbcf"`

We need to find the longest sequence of characters that can be formed by deleting zero or more characters from `str1` AND by deleting zero or more characters from `str2`, such that the remaining characters are identical in both and their order is preserved.

Let's look at a few common subsequences:

* `"a"` (Length 1)
* `"c"` (Length 1)
* `"f"` (Length 1)
* `"ac"` (Length 2) - From `str1`: **a**_b_**c**_daf_ ; From `str2`: **a**_c_**c**_f_
* `"af"` (Length 2) - From `str1`: **a**_bcda_**f** ; From `str2`: **a**_cb_**f**

Now, consider **`"abcf"`** (Length 4):
* Can we form `"abcf"` from `str1 = "abcdaf"`? Yes, by taking `a`, `b`, `c`, `f` and deleting `d, a`. (i.e., **abc**_da_**f**)
* Can we form `"abcf"` from `str2 = "acbcf"`? Yes, by taking `a`, `b`, `c`, `f` and deleting `c`. (i.e., **a**_c_**bcf**)

Since `"abcf"` is the longest subsequence of both `str1` and `str2`, it is the **Longest Common Subsequence**.