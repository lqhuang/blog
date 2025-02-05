---
title: 'Unbuffered I/O Can Make Your Rust Programs Much Slower'
date: 2022-01-07
tags:
  - rust
  - til
  - python
  - dev
---

1. Use `strace` and `perf` to count how many syscalls were invoked.
2. Yeah, Rust actually supports file I/O without buffer. It's may more simple in
   some situtations

> ## Conclusion
>
> In this post, we saw that:
>
> - System calls in Linux are slower than regular functions
> - Issuing too many syscalls can have very negative effects on run-time
>   performance
> - By using `BufReader` and `BufWriter`, we can amortize the cost of syscalls
> - Even experienced programmers can miss these issues
> - We can use `strace` and `awk` to find if and where unbuffered I/O happens in
>   our programs
>
> From:
> [Unbuffered I/O Can Make Your Rust Programs Much Slower](https://era.co/blog/unbuffered-io-slows-rust-programs)
