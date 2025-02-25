---
title: Bundling binary tools in Python wheels
date: 2022-06-18
tags:
  - tools
  - python
---

`zig cc` could be a smaller, easy-installed and full featured frontend of Clang.
What you only need to do is just `pip install ziglang` when you're not
convenient to use `gcc` or `clang`. Cross platform build will benefit from this
a lot.

> `zig cc` is _not the main purpose of the Zig project_. It merely exposes the
> already-existing capabilities of the Zig compiler via a small frontend layer
> that parses C compiler options.

Another two cents:

- Other tools could be also installed from `pip`, such as `nodejs`.
- Zig's Linux tarballs are fully statically linked. And it's also easy to build
  target with different `glibc` (eg: `-target x86_64-linux-gnu.2.28`,
  `-target x86_64-linux-musl`). Pretty good that host and target are decoupled.

Ref:

- [Bundling binary tools in Python wheels](https://simonwillison.net/2022/May/23/bundling-binary-tools-in-python-wheels)

Further readings:

- [How Uber Uses Zig](https://jakstys.lt/2022/how-uber-uses-zig/)
- [`zig cc`: a Powerful Drop-In Replacement for GCC/Clang](https://andrewkelley.me/post/zig-cc-powerful-drop-in-replacement-gcc-clang.html)
