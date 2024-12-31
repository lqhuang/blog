---
title: Introducing Immortal Objects for Python
date: 2023-08-19
tags:
  - python
  - good-reading
---

Instagram has introduced PEP-683 Immortal Objects to their Python codebase
(custom Django and custom Python interpreter) and achieve improvements in both
memory and CPU efficiency of handling our requests by reducing copy on writes.

Refs:

- [Introducing Immortal Objects for Python](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/)
- [lqhuang.io Note - PEP 683 – Immortal Objects, Using a Fixed Refcount](https://lqhuang.io/note/immortal-objects-using-a-fixed-refcount)
