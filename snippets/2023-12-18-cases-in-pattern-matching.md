---
title: Syntax Style in Python Pattern Matching
date: 2023-12-18
tags:
  - python
  - dev
---

WIP

```python
match obj:
    case int(0): ...  # special case for 0
    case int(): ...   # any other int
    case float(): ... # any float
    case _:           # anything else
```

```python
match obj:
    case int as i: ...   # can this work?
    case int(i): ...     # `i` will be `0` in the later context
    case int() as i: ... # any other example from official doc
    case _:              # anything else
```

I would prefer `case int() as i` over `case int(i)`?

Becase the later one feels like `i` is still unconverted to `int` yet?

- https://peps.python.org/pep-0634/#class-patterns
