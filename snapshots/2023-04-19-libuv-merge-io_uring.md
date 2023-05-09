---
title: libuv merges io_uring with an 8x increase in throughput
date: 2023-04-19
tags:
  - news
  - dev
---

A PR to introduce initial support of `io_uring` for libuv has been merged. A lot
of downstream projects (nodejs, uvicorn, etc) will benefit from it.

> Add io_uring support for several asynchronous file operations. io_uring is
> used when the kernel is new enough, otherwise libuv simply falls back to the
> thread pool.
>
> Performance looks great; an 8x increase in throughput has been observed.
>
> This work was sponsored by ISC, the Internet Systems Consortium.

- [linux: introduce io_uring support #3952](https://github.com/libuv/libuv/pull/3952)
- [Tweet status from @axboe](https://twitter.com/axboe/status/1648331118461202433)
