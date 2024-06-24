---
title:
  An Example of Covariance, Contravariance and Invariance in Python Type Hints
date: 2023-12-12
tags:
  - python
  - dev
  - functional-programming
---

Qiangning Hong (@hongqn) share a Python type annotation tip on X (Twitter), and
raised discussions about covariance, contravariance and invariance in Python

```python
from collections.abc import Sequence

a: list[str] =["a"]

def f1(a: list[int | str]): pass
def f2(a: Sequence[int | str]): pass

f1(a)  # incompatible type assignment
f2(a)  # compatible
```

So why?

The key point is that `list[int | str]` is not covariant with `list[str]`, while
`Sequence[int | str]` is covariant with `list[str]`.

The reason of `Sequence` is immutable and is also covariant, most immutable
containers are covariant, so `f2` cannot modify the list even if it is passed as
a list.

`List` is mutable, so if the parameter is declared as a list type, `list[str]`
and `list[int | str]` are two different types. In type system, mutable types
usually are invariant (e.g. `MutableSequence`, `list`, `set` in Python).

It would be more clear that we add an function to accept `Sequence` type, and it
will be compatible with variable `a`:

```python
def f3(a: Sequence[str]): pass

f3(a)  # compatible
```

Refs:

- [Tweets from @hongqn](https://twitter.com/hongqn/status/1734062019450638518)
- [Tweets from @frostming90](https://twitter.com/frostming90/status/1734076523286540554)
- [Tweets from @laixintao](https://twitter.com/laixintao/status/1734270644911775795)
- [Covariance, Contravariance, and Invariance — The Ultimate Python Guide](https://blog.daftcode.pl/covariance-contravariance-and-invariance-the-ultimate-python-guide-8fabc0c24278)
- [PEP 483 – The Theory of Type Hints: Covariance and Contravariance](https://peps.python.org/pep-0483/#covariance-and-contravariance)
- [Wikipedia - Covariance and contravariance (computer science)](https://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29)
