---
title: Beware of fast-math
date: 2023-10-25
tags:
  - til
  - system-programming
---

fast-math is a set of compiler flags that enables a series of optimizations for
floating-point arithmetic.

- `-ffast-math` (and included by `-Ofast`) in GCC and Clang
- `-fp-model=fast` (the default) in ICC
- `/fp:fast` in MSVC
- `--math-mode=fast` command line option or `@fastmath` macro in Julia.

But please notice that fast-math is not free lunch. Use it with cautions 😲.

Hence check this post [^simon] to see what innocuous performance speedup or
unfortunate downstream effects fast-math would bring to you.

> I mean, the whole point of fast-math is trading off speed with correctness. If
> fast-math was to give always the correct results, it wouldn’t be fast-math, it
> would be the standard way of doing math. -- Mosè Giordano [^giordano]

[^simon]: [Simon's notes - Beware of fast-math](https://simonbyrne.github.io/notes/fastmath/)
[^giordano]: [What’s going on with exp() and –math-mode=fast?](https://discourse.julialang.org/t/whats-going-on-with-exp-and-math-mode-fast/64619/7)
