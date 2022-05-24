---
title: "Initial JSON Type Support in Python"
date: 2022-05-21
tags:
  - python
---

Because typing system in Python lacks of recursive type, we can not annotate
JSON-like data for type hints. Recently, There is a progress that an
experimental `JSON` type has been implemented under `_typeshed` lib.

Try it like:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import JSON
```

Of course, we still need to wait offical `JSON` type support.

> [Define a JSON type #182](https://github.com/python/typing/issues/182#issuecomment-1133611222)
