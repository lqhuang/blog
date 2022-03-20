---
title: "Why I use attrs instead of pydantic"
date: 2021-08-26
tags:
  - recommended-reading
  - Python
---

文章作者作为 cattrs 的开发者 (利益相关) 比较了 attrs 相比 pydantic 的优点.

在个人使用体验上

- validation 可能不是必须的..这点上 attrs 做得更好..
- pydantic 的序列化确实是个坑, 但是 cattr 需要额外 converter 申明也很麻烦..

大部分还比较客观, pydantic 提供了很多很 fancy 的功能, 其实 c/attrs 实现和定义上
更简洁, 但是架不住 pydantic 还是更加流行.

祝愿 attrs + cattrs 发展快一些，好让我替换 pydantic.

> [Why I use attrs instead of pydantic](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic)

Updated at 2021-12-15:

Pendulum 下 Superclass 的序列化问题已经解决
(https://github.com/samuelcolvin/pydantic/pull/1291)

但是反序列化依然不正确

```python
from pydantic import BaseModel
from pendulum import DateTime

class PydanticPendulum(BaseModel):
        a: DateTime

b = PydanticPendulum(a='2021-05-25T00:00:00')

assert isinstance(b.a, DateTime)  # failed
```
