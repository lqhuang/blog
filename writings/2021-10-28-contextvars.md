---
title: Local Variable in Async Environments -- `contextvars`
created: 2021-10-28
updated: 2021-10-28
draft: true
tags:
  - python
---

Context variables are convenient when you need to pass a variable along the
chain of calls so that they share the same context, in the case when this cannot
be done through a global variable in case of concurrency. Context variables can
be used as an alternative to global variables both in multi-threaded code and in
asynchronous (with coroutines).

如果单独创建一个 `Context` 类的，会是个完全空的 context

```
init_ctx = Context()
```

immutable dictionary implementation Hash Array Mapped Tries (HAMT) Files of
interest: `Python/hamt.c` and `Include/internal/hamt.h`

`contextvars` pure python implementation:
https://github.com/MagicStack/contextvars

Refs:

- https://www.python.org/dev/peps/pep-0567/
- https://docs.python.org/3/library/threading.html#threading.local
- https://www.python.org/dev/peps/pep-0550/
- https://docs.python.org/3/library/contextvars.html
- https://stackoverflow.com/questions/63105799/understanding-python-contextvars

Next step: https://www.python.org/dev/peps/pep-0568/

## Practices

Use contextvar to write a thread-safe LocalStack

## Refs

- https://github.com/pallets/werkzeug/blob/main/src/werkzeug/local.py
- https://www.cnblogs.com/traditional/p/17403428.html
- https://photonlines.substack.com/p/grokking-hash-array-mapped-tries
- https://thiagowfx.github.io/2024/01/synchronized-in-python/
