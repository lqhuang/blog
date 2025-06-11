---
title: "Rewriting a Language's Compiler in Itself"
date: 2025-02-05
tags:
  - rust
  - zig
  - system-programming
draft: true
src: https://gist.github.com/rtfeldman/77fb430ee57b42f5f2ca973a3992532f
---

The creator of Roc lang is rewriting the compiler in itself and Zig lang instead of previous rust, and he's documenting the process and answering the questions:

- [Rewriting a Language's Compiler in Itself](https://gist.github.com/rtfeldman/77fb430ee57b42f5f2ca973a3992532f)

It's a pretty good reading material about how to choose programming languages to write "language". RIIR (rewrite it in Rust) starts to be a "strange" movement. Roc lang's decision to move away from Rust has obviously attracted a lot of attention and discussion in the programming community.

I think he is basically right, at least at the compiler writing level. Especially since, although Rust has a quite large ecosystem, it still lacks long-standing and industry level fundamental libraries.

Another point that impressed me is the convenience of the Zig toolchain and the interaction between Zig and LLVM. What an awesome sweet spot for writing compilers!
