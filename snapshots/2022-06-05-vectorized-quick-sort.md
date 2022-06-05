---
title: Vectorized and Performance-portable Quicksort
date: 2022-06-05
tags:
  - hpc
  - news
---

Jeff Dean quotes about a state-of-art vectorized quicksort algorithm developed
by Google AI researcher Jan Wassenberg. They have tested it can be ten times
faster than `std::sort` in C++.

> Today we're sharing open source code that can sort arrays of numbers about ten
> times as fast as the C++ `std::sort`, and outperforms state of the art
> architecture-specific algorithms, while being portable across all modern CPU
> architectures.

References:

1. [Jeff Dean's status](https://twitter.com/JeffDean/status/1533124158686580737)
2. [Vectorized and Performance-portable Quicksort](https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html)
3. [google/highway](https://github.com/google/highway)
4. [[2205.05982] Vectorized and performance-portable Quicksort](https://arxiv.org/abs/2205.05982)
