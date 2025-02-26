---
title: SIMD in Pure Python
date: 2024-01-13
tags:
  - python
  - simd
  - good-reading
---

1. Python Has infinite precision integers (Python also has a `bytearray` type)
2. Python has bitwise operation (`&`, `|`, `^`, `~`, `<<`, `>>`)
3. Leverage compiler optimizations (CPython compiles your code into a bytecode
   format)

That's enough to implement simple SIMD operations in pure Python.

Awesome!

References:

- [SIMD in Pure Python](https://www.da.vidbuchanan.co.uk/blog/python-swar.html)
- [Bitslicing, An Introduction](https://timtaubert.de/blog/2018/08/bitslicing-an-introduction/)
