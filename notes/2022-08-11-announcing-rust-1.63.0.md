---
title: Announcing Rust 1.63.0
date: 2022-08-11
tags:
  - rust
  - news
---

Rust team is annoucing 1.63.0 stable today [^1].

There are serveral features I quite interested in:

1. Scoped threads [^2]
2. Safety I/O [^3]
3. global `const` initialization for Mutex, RwLock, Condvar

These features help a lot to simplify codes. Also my next forwarding features
should be:

1. keyword generics [^4][^5]
2. GATs [^6]
3. async traits [^7]

References:

[^1]: [Announcing Rust 1.63.0](https://blog.rust-lang.org/2022/08/11/Rust-1.63.0.html)
[^2]: [rfcs: scoped-threads](https://github.com/rust-lang/rfcs/blob/master/text/3151-scoped-threads.md)
[^3]: [rfcs: io-safety](https://github.com/rust-lang/rfcs/blob/master/text/3128-io-safety.md)
[^4]: [Announcing the Keyword Generics Initiative](https://blog.rust-lang.org/inside-rust/2022/07/27/keyword-generics.html)
[^5]: [Async overloading](https://yosh.is/writing/async-overloading)
[^6]: [rfcs: Generic Associated Types](https://github.com/rust-lang/rfcs/blob/master/text/1598-generic_associated_types.md)
[^7]: [rfcs: async_fn_in_traits](https://github.com/rust-lang/rfcs/blob/master/text/3185-static-async-fn-in-trait.md)
