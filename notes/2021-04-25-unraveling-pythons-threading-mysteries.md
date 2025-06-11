---
title: Unraveling Pythons Threading Mysteries
date: 2021-04-25
tags:
  - python
  - good-reading
---

### Part 1: Unraveling Pythons Threading Mysteries

前半部分比较简单, 比较了 threading 和 multiprocessing 的区别. Threading 怎么都不
是正确的 CPU-bound parallelization. (比较奇怪的是, 为什么 ThreadPoolExecutor 固
定比 Treading 长两倍的时间)

后半部分有两个内容比较有意思

1. multiprocess 在创建新的 Process 时 python interpreter 是怎么从父进程获取变量
   的: `spawn` 和 `fork` 两个模型。引入了
   `inherited = copied, and not_inherited = re-evaluated` 的想法。`spawn` 只
   inherit necessary resources，所以反而需要 re-evaluate 来获取大部分变量。而且
   `fork` 可以通过 copy 来获得变量资源。

2. GIL 是在 bytecode 层面上的 lock, 只能同时执行某一线程的字节码. 可以利用 `dis`
   模块查看 statement 的 bytecode. 同时解释了 Python 的 GIL 在 bytecode 上是怎么
   导致 race condition 的 (`sys.setcheckinterval()`)

> [Unraveling Python's Threading Mysteries](https://towardsdatascience.com/unraveling-pythons-threading-mysteries-e79e001ab4c)

### Part 2: what the GIL is

全文有点长, 讲述了 Python 下 threading model 的起源与思考, Python 的 threading
是 share everything 的.

摘录一段关于 GIL 很准确的描述:

> The GIL is an interpreter-level lock. This lock prevents execution of multiple
> threads at once in the Python interpreter. Each thread that wants to run must
> wait for the GIL to be released by the other thread, which means your
> multi-threaded Python application is essentially single threaded, right? Yes.
> Not exactly. Sort of.

> CPython uses what's called "operating system" threads under the covers, which
> is to say each time a request to make a new thread is made, the interpreter
> actually calls into the operating system's libraries and kernel to generate a
> new thread. This is the same as Java, for example. So in memory you really do
> have multiple threads and normally the operating system controls which thread
> is scheduled to run. On a multiple processor machine, this means you could
> have many threads spread across multiple processors, all happily chugging away
> doing work.

> However, while CPython does use operating system threads (in theory allowing
> multiple threads to execute within the interpreter simultaneously), the
> interpreter also forces the GIL to be acquired by a thread before it can
> access the interpreter and stack and can modify Python objects in memory all
> willy-nilly. The latter point is why the GIL exists: The GIL prevents
> simultaneous access to Python objects by multiple threads. But this does not
> save you (as illustrated by the Bank example) from being a lock-sensitive
> creature; you don't get a free ride. The GIL is there to protect the
> interpreters memory, not your sanity.

> The GIL also keeps garbage collection (the reason you don't have to worry
> about memory management, you bum) working. It prevents one thread from
> decrementing the counters for an object and letting the object go into the
> ether while another object is working with that object. Python's garbage
> collection (deallocating unused objects to free memory) utilizes the concept
> of reference counting. This is where all references to a given object
> (integer, string or ''YourCat(object)'') are tracked. When the number of
> references reaches zero, the object is deleted. The GIL prevents any two
> threads from decrementing the reference count to any object to 0 while another
> thread is working on that object. Remember, only one thread can access a
> Python object at a time.

> [PYTHON THREADS AND THE GLOBAL INTERPRETER LOCK](http://jessenoller.com/blog/2009/02/01/python-threads-and-the-global-interpreter-lock)
