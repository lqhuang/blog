---
title: local variable in async environment -- contextvars
---




Context variables are convenient when you need to pass a variable along the chain of calls so that they share the same context, in the case when this cannot be done through a global variable in case of concurrency. Context variables can be used as an alternative to global variables both in multi-threaded code and in asynchronous (with coroutines).





如果单独创建一个 `Context` 类的，会是个完全空的 context

```
init_ctx = Context()
```



immutable dictionary implementation
Hash Array Mapped Tries (HAMT)
Files of interest: `Python/hamt.c` and `Include/internal/hamt.h`


`contextvars` pure python implementation: https://github.com/MagicStack/contextvars



Refs:
https://www.python.org/dev/peps/pep-0567/
https://docs.python.org/3/library/threading.html#threading.local
https://www.python.org/dev/peps/pep-0550/
https://docs.python.org/3/library/contextvars.html

https://stackoverflow.com/questions/63105799/understanding-python-contextvars

Next step:
https://www.python.org/dev/peps/pep-0568/
