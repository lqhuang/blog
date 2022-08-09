---
title: "Crimes with Python's Pattern Matching"
date: 2022-08-06
tags:
  - python
  - til
---

Today, I learn some wired tricks in Python's pattern matching :lol:

> You can match on arrays, dictionaries, and custom objects. To support matching
> objects, Python uses `isinstance(obj, class)`, which checks
>
> 1. If `obj` is of type `class`
> 2. If `obj` is a transitive subtype of `class`
> 3. If `class` is an ABC and defines a `__subclasshook__` that matches the type
>    of `obj`.
>
> Ref:
> [Crimes with Python's Pattern Matching](https://www.hillelwayne.com/post/python-abc/)
