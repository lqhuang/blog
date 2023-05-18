---
title: Real Multithreading is Coming to Python - Learn How You Can Use It Now
date: 2023-05-16
tags:
  - python
---

Simon Willison introduces an article[^1] about how to use Multithreading feature
in latest Python mainline.

> Martin Heinz provides a detailed tutorial on trying out the new
> Per-Interpreter GIL feature that’s landing in Python 3.12, which allows Python
> code to run concurrently in multiple threads by spawning separate
> sub-interpreters, each with their own dedicated GIL.
>
> It’s not an easy feature to play with yet! First you need to compile Python
> yourself, and then use APIs that are generally only available to C code.

As he mentioned, there is also an implementation of `RecvChannel` and
`SendChannel` classes to create channels for exchanging data (?) which fits
Armin's prediction[^3].

> My strong hunch is that the GIL does not need removing, if a) subinterpreters
> have their own GILs and b) an efficient way is provided to pass (some) data
> between subinterpreters lock free and c) we find good patterns to make working
> with subinterpreters work.
>
> -- Armin Ronacher (@mitsuhiko)

PS: I'm also planning a framework inspired from Actor model for multithreading
Python. Working on that 😭.

Refs:

- [^1][Real Multithreading is Coming to Python - Learn How You Can Use It Now](https://martinheinz.dev/blog/97)
- [Tweet status from @simonw](https://twitter.com/simonw/status/1658200421553553408)
- [Tweet status from @mitsuhiko](https://twitter.com/mitsuhiko/status/1645747519782092806)
