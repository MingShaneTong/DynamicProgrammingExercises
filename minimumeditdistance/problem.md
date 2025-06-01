# Minimum Edit Distance Problem

## Problem Description

The Minimum Edit Distance problem (also known as Levenshtein Distance) is a fundamental problem in computer science and computational linguistics. It calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another.

**Key operations allowed:**
* **Insertion:** Add a character.
* **Deletion:** Remove a character.
* **Substitution:** Change one character to another.

Each of these operations typically costs 1. The goal is to find the sequence of operations with the lowest total cost.

This problem has wide applications in areas like spell checkers, DNA sequence analysis, plagiarism detection, and natural language processing.

## Example

Let's illustrate the problem with a simple example:

**Given:**
* `word1 = "kitten"`
* `word2 = "sitting"`

**Required Edits:**

1.  `k`itten -> `s`itten (substitution of 'k' with 's')
2.  sitt`e`n -> sitt`i`n (substitution of 'e' with 'i')
3.  sitting -> sitting`g` (insertion of 'g')

The sequence of operations is: **Substitution, Substitution, Insertion.**
The total number of edits required is **3**. Therefore, the minimum edit distance between "kitten" and "sitting" is 3.
