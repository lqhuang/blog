---
title: Python 类实例化的完整流程
created: 2021-09-23
updated:
tags:
  - python
draft: true
---

`metaclass`

`__post_class__`?

`__new__`

`__mro__`

`__subclasshook__`

什么是 "virtual subclasses"

从执行 `__init__` 前后有什么额外检查/注入等等其他黑魔法。

子类实例化时是否还有其他问题等等

1. <https://github.com/python/cpython/blob/main/Lib/_collections_abc.py>
2. https://github.com/python/cpython/blob/main/Lib/abc.py
3. https://twitter.com/mathsppblog/status/1543964703432605696
4. https://blog.wh2099.com/python/c3-mro
5. https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/
6. https://sunisdown.me/python-yuan-lei.html
7. https://developer.ibm.com/tutorials/ba-metaprogramming-python/
8. https://snarky.ca/unravelling-pythons-classes/
9. https://til.simonwillison.net/python/init-subclass
10. https://github.com/MoserMichael/python-obj-system/blob/master/python-obj-system.md
11. https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
12. https://amr-khalil.medium.com/a-deep-dive-into-the-new-method-in-python-25e4cb5d1361
13. https://blog.allsunday.io/posts/2014-11-09-python-mutiple-metaclass/

