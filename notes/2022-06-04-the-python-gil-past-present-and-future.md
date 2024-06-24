---
title: "The Python GIL: Past, Present, and Future"
date: 2022-06-04
tags:
  - python
  - good-reading
---

We have known the past and present of GIL in Python, what is about the future?

I'm really looking forward to

> GIL-less CPython with minimal backward incompatibilities at both the Python
> and C layers

And

> At a high level, the removal of the GIL is afforded by changes in three areas:
> the memory allocator, reference counting, and concurrent collection
> protections.

1. Memory Allocators: `mimalloc` is a general purpose, highly efficient,
   thread-safe memory allocator which is worthy of an in-depth look. The nogil
   project utilizes these structures for the implementation of dictionaries and
   other collection types which minimize the need for locks on non-mutating
   access.
2. Reference Counting:
   - For immortal objects, nogil utilizes the least significant bits of the
     object’s reference count field for bookkeeping, nogil can make the
     refcounting macros no-op for these objects, thus avoiding all contention
     across threads for these fields. nogil also uses a form of biased reference
     counting to split an object’s refcount into two buckets. The thread that
     owns the object can then combine this local and shared refcount for garbage
     collection purposes, and it can give up ownership when its local refcount
     goes to zero.
   - For objects are typically owned by multiple threads and are not immortal, a
     deferred reference counting scheme is employed. The utility of this
     technique is limited to objects that are only deallocated during garbage
     collection because they are typically involved in reference cycles.
3. Concurrent Collection Protections: The third high-level technique that nogil
   uses to enable concurrency is to implement an efficient algorithm for locking
   container objects, such as dictionaries and lists, when mutating them.

Wish the future is coming soon!

> [The Python GIL: Past, Present, and Future -- Barry Warsaw](https://www.backblaze.com/blog/the-python-gil-past-present-and-future/)
>
> [Faster CPython](https://faster-cpython.readthedocs.io),
> [Github - faster-cpython](https://github.com/faster-cpython)
