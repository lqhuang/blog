---
title: "PEP 690 – Lazy Imports"
date: 2022-05-14
tags:
  - python
---

IMHO, I like lazy imports as a fancy and powerful **opt-in** feature, but it's
quite doubtful to set this feature enabled by default in current proposal (PEP
690).

Implicit behaviors are terrible and will obviously break backward compatibility.

Do we forget the Zen of Python: "Explicit is better than implicit"?

> [PEP 690 – Lazy Imports](https://peps.python.org/pep-0690)
>
> [Discussions | PEP 690 Lazy Imports](https://discuss.python.org/t/pep-690-lazy-imports/15474)

Update 2022-07-05:

An article about how Meta use lazy imports to speed up Instagram Python server's
slowdown caused by complex dependency hell.

> [Python Lazy Imports With Cinder](https://developers.facebook.com/blog/post/2022/06/15/python-lazy-imports-with-cinder)
