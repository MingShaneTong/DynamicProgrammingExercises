# 0/1 Knapsack Problem

This document explains the classic **0/1 Knapsack Problem**, a fundamental problem in computer science and a common example used to illustrate algorithmic techniques like dynamic programming.

## The Problem Statement

Imagine you're a hiker preparing for a trip. You have a **knapsack** with a **limited weight capacity**. You also have a list of various items you could potentially take, but each item has two properties: a **weight** and a **value**.

Your goal is to choose a combination of items to put into your knapsack such that:

1.  The **total weight** of the chosen items does **not exceed** the knapsack's capacity.
2.  The **total value** of the chosen items is as **large as possible**.

## Why "0/1"?

The "0/1" in the name is crucial and refers to the decision you make for each item:

* **0 (Zero):** You **do not** take the item.
* **1 (One):** You **do** take the item.

This means you cannot take only a *fraction* of an item, nor can you take the *same item multiple times*. It's an all-or-nothing decision for every item on your list.

## Key Characteristics

* **Optimization Goal:** We're trying to find the *maximum* possible total value.
* **Capacity Constraint:** There's a strict limit on the total weight you can carry.
* **Discrete Choices:** For each item, you only have two distinct options: take it or leave it.

This problem is a great example of a situation where making the "locally best" choice (e.g., always picking the item with the highest value-to-weight ratio) doesn't guarantee the overall best solution, making it a perfect candidate for more sophisticated algorithmic approaches.

