---
title: io_uring and seccomp
date: 2024-10-13
tags:
  - io_uring
  - system-programming
---

Till now I just known that `io_uring` is not enabled by default while using container (in the past day XD).

> A side effect is that io_uring effectively bypasses the protections provided by seccomp filtering — we can't filter out syscalls we never make! This isn't a security vulnerability per se, but something you should keep in mind if you have especially paranoid seccomp rules. [^seccomp]

Fortunately, moby and containerd have already added allow list for `io_uring` in seccomp filters. [^moby][^containerd]

But [@tgross](https://blog.0x74696d.com) still suggest to to check up on if you're expecting seccomp filtering to harden your applications.

[^seccomp]: [io_uring and seccomp | 0x74696d](https://blog.0x74696d.com/posts/iouring-and-seccomp/)
[^moby]: [seccomp: whitelist io-uring related system calls #39415](https://github.com/moby/moby/pull/39415)
[^containerd]: [seccomp: allow io-uring related system calls #4493](https://github.com/containerd/containerd/pull/4493)
