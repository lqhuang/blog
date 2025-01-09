---
title: Structure Concurrency in Python
created: 2021-11-03
updated: 2021-11-03
tags:
  - python
  - concurrency
draft: true
---

trio

结构性并发

Tasks

https://realpython.com/python311-exception-groups/

https://iscinumpy.dev/post/python-311/#asyncio

> Haskell
>
> 超时、线程 kill 信号、键盘的 kill 信号都是异步异常，异步异常就是不是在本线程中
> 抛出的异常，而是其他线程在本线程任意一点可能引起的异常。

https://blog.ibyte.me/post/structured-concurrency

asyncio 虽然是同线程下的机制, 但是可能还需要一些 sync barrier 来保障任务的顺序.

在 asyncio.gather 的使用过程中遇到了一些先后完成乱序的数据竞争
