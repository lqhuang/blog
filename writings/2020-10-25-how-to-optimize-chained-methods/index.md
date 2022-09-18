---
title: combined streaming operators 是如何减少中间过程的
created: 2020-10-25
tags:
  - python
  - functional-programming
draft: true
---

Scala

```scala
reduce(map(a, power(abs(_),p)), _ + _)
```

map can be combined with `reduce` to avoid intermediate collections.

同样的例子还存在 pandas 里

chain method 是如何解析，尽量减少中间过程落盘的呢

对象链式调用方法如何优化中间过程？(新生成对象/inplace change)

Pandas 利用缓式评估（lazy evaluation）可能出现在方法链中

函数式和 OOP 在处理这个问题上有什么异同点

分布式系统里的幂等是怎么设计的

example

经过一句话点拨和之前看了一个 pandas 的源码

chain method

只是生成了一个新的 BuilderClass

里面记录了数据在哪里, 和要对数据做什么处理

因此, 调用这个 method 并不产生实际的复杂计算

可以叠加 operations, 等最后 emit 以后, 再针对过程进行优化或者 dag 进行处理.
