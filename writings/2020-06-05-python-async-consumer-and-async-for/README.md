---
title: '更加 "并发" 的 asyncio'
created: 2020-06-05
keywords:
  - python
draft: true
---

## Introduction

Python 在 3.4 中引入了标准库 `asyncio`，算是正式引进了异步编程的基础设施到
Python 之中，在 3.6 以后逐渐正式稳定下来异步的关键词和 API 接口。异步编程范式通
过非阻塞 (non-block) 的形式释放执行权提高了 Python 的并发能力 (concurrency)，期
望以同步的书写习惯达到替代回调形式 (callback) 的非阻塞编程。但是异步并不意味着天
然的非阻塞，不正确地使用异步接口，可能还是会导致阻塞代码的行为，同时异步也不比总
是自发形成高并发，使用异步关键词依然有可能写出不是很高效的代码。

比如，以官方文档中示例

```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    tic = time.time()

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(
        f"finished at {time.strftime('%X')}, elapsed time: {time.time() - tic}s"
    )


asyncio.run(main())
```

和

```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    tic = time.time()

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Nothing happens if we just call
    #     task1 = say_after(1, 'hello')
    #     task2 = say_after(2, 'hello')
    # two coroutine objects are created but not awaited,
    # so it *won't run at all*.
    # Of course, another option in this situation is to use
    #     await asyncio.gather(*(task1, task2))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(
        f"finished at {time.strftime('%X')}, elapsed time: {time.time() - tic}s"
    )


asyncio.run(main())
```

第一段代码其实相对来说还是阻塞的，执行时间为 3s，而第二段才是真正进行了非阻塞的
执行。

## 反直觉的异步执行

非常类似的场景是在多个函数或者协程 (coroutine) 中相互调用的时候，有时候也不是那
么的 "异步"

```python
import time
import asyncio


async def g():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    tic = time.time()
    async for x in g():
        print(x)
        await asyncio.sleep(2)
    print(f"elapsed time: {time.time() - tic}s")


asyncio.run(main())
```

类似但是更抽象的场景可以视为生产者 (Producer) 和消费者 (Consumer) 的模式:

```python
import time
import asyncio


async def producer(total):
    for i in range(total):
        print(f"Producer: create event A0 -> {i}")
        await asyncio.sleep(i)
        yield i


async def consumer(source):
    async for i in source:
        d = 2 * i
        print(f"Consumer: process event {i} -> {d}")
        await asyncio.sleep(2 * i)
        yield d


async def main():
    tic = time.time()
    async for i in consumer(producer(5)):
        print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
```

在以上的代码中， `asyncio.sleep` 的时间切片并不是共享的，是实实在在的阻塞代码，
没有体验到使用 `async` 的异步带来的好处。

如何进行改造呢? 可以增加一个队列在进行信息存储和交换

```python
import time
import asyncio


async def g():
    for i in range(5):
        print(f"Producer: create event A{i} -> {i}")
        await asyncio.sleep(i)
        yield i


async def producer(queue):
    async for i in g():
        await queue.put(i)
    await queue.put(None)


async def consumer(queue):
    while (x := await queue.get() is not None):
        d = 2 * x
        print(f"Consumer: process event B{x} -> {x} * 2 = {d}")
        await asyncio.sleep(d)


async def main():
    tic = time.time()
    queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue),
        return_exceptions=False,
    )

    print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
```

如果有多个 worker 的话，将会变得相对复杂些。

```python
import time
import asyncio


async def g():
    for i in range(10):
        print(f"Producer: create event A{i} -> {i}")
        await asyncio.sleep(i * 0.1)
        yield i


async def producer(queue):
    async for i in g():
        await queue.put(i)


async def consumer(queue: asyncio.Queue):

    while True:
        x = await queue.get()
        d = 2 * x
        print(f"Consumer: process event B{x} -> {x} * 2 = {d}")
        await asyncio.sleep(d * 0.2)
        queue.task_done()  # to notify queue.join() task is completed


async def main():
    tic = time.time()
    queue = asyncio.Queue()

    producer_group = [asyncio.create_task(producer(queue)) for _ in range(4)]
    consumer_group = [asyncio.create_task(consumer(queue)) for _ in range(6)]

    await asyncio.gather(*producer_group, return_exceptions=False)

    print("Before join: done producing.")
    await queue.join()
    print("After join: If you don't use `task_done()` you wouldn't see this.")

    for t in consumer_group:
        t.cancel()

    print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
```

但是这种方式还是回调型的思想，需要侵入式地在 producer 和 consumer 里面定义回调函
数。

相比之下，可以用 `async geneator` 更彻底的从回调形式转化为同步代码的思维。

```python
import time
import itertools
import asyncio


async def producer(total):
    for i in range(total):
        print(f"Producer: create event A0 -> {i}")
        await asyncio.sleep(i)
        yield i


async def consumer(source):
    async for i in source:
        d = 2 * i
        print(f"Consumer: process event {i} -> {d}")
        await asyncio.sleep(2 * i)
        yield d


async def main():
    tic = time.time()
    async for i in consumer(producer(5)):
        print(f"Output  : output event B{i} -> {i}")
        print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
```

## "小孩子才做选择，我全都要"

## References:

- https://docs.python.org/dev/library/asyncio-task.html
- https://stackoverflow.com/questions/56902202/python-async-generator-not-async
- https://www.educative.io/blog/python-concurrency-making-sense-of-asyncio
- https://gist.github.com/vxgmichel/4ea46d3ae5c270260471d304a2c8e97b
- https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/#websocket-servers
- https://realpython.com/async-io-python/
- https://stackoverflow.com/questions/49637086/python-what-is-queue-task-done-used-for
- https://realpython.com/queue-in-python/#using-thread-safe-queues
- Rich examples for queue
- https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3.html
- Merge async streaming
- https://stackoverflow.com/questions/51399339/appending-to-merged-async-generators-in-python/51403277#51403277
