---
title: Why do Rust packages have any dependency on C code?
date: 2023-12-01
tags:
  - rust
  - clang
  - good-reading
---

Alexis King [^thread] is one of my most advocated programmers in PL community.
She is doing great! 🥰

Here is a fun and informative answer [^ans] wrote by Alexis for _Why do common
Rust packages depend on C code?_. So I just post it as a recommendation.

Basically, the TL;DR points are:

- C ABIs
- C is your operating system’s interface
- C ABIs are difficult to separate from the C language
- C ABIs are difficult to separate from C toolchains

[^thread]: [Tweet from @lexi_lambda](https://twitter.com/lexi_lambda/status/1728919289430962485)
[^ans]: [StackOverflow - Why do common Rust packages depend on C code?](https://langdev.stackexchange.com/a/3237)
