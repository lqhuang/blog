---
title: 'The Hidden Cost of Software Libraries'
date: 2025-10-26
tags:
  - til
  - clang
  - rust
---

> Turns out the Rust version with clap is **50x SLOWER**! 54.41 to be exact. [^ref]
>
> Rust usually runs close to C speeds for equivalent implementations, so the speed difference is likely all overhead from the library.
>
> 50x hit to performance. Just so you can have some magic macros for your command line interface.

TIL, `clap` will slow down the startup times. But it's just call only "once" while parsing aruments.

Sort of balance between usablitiy and extre performace?

[^ref]: [The Hidden Cost of Software Libraries - by dechichi](https://cgamedev.substack.com/p/the-hidden-cost-of-software-libraries)
