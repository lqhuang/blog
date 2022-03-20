---
title: "Deep Dive into Flask's Application and Request Contexts"
date: 2021-12-15
tags:
  - Python
---

Highlight:

> The `current_app` and `request` proxies are not actually global variables;
> they point to global objects that are implemented as context-locals, so the
> proxies are always **unique** to each worker.
> https://testdriven.io/blog/flask-contexts-advanced/
