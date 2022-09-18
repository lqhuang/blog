---
title: GATs (Generic Associated Types)
created: 2020-12-21
tags:
  - rust
  - functional-programming
draft: true
---

关注 GAT

不如先来了解下关联类型 Associated types

2、具体类型由 callee 来决定的，使用关联类型。

一般用在方法返回值处中（Into trait 也是个特例）：

因为 callee 中的类型，是在实现时就确定下来的。对于确定的泛型和 Self，它就是唯一
的。所以它并没有多态性，如果放在 method 参数上，要放不同的类型的参数，就要写多个
类似的结构，所以一般不会用在 method 的参数上。这样也解释了为什么 FnOnce trait 为
什么要将返回类型设计为关联类型，当一个闭包写下来的时候，其返回类型是确定的，而且
还有一个重要的原因是，rust 没有 scala 那样的子类型关系，所以无法进行类似的推导。

GATs example:

GATs application

Ref:

1. https://zhuanlan.zhihu.com/p/113067733
2. https://www.fpcomplete.com/blog/monads-gats-nightly-rust/
3. https://www.reddit.com/r/rust/comments/k4vzvp/gats\_on\_nightly/
