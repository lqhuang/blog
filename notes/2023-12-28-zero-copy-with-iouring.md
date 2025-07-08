---
title: Zero-copy network transmission with io_uring
date: 2023-12-28
tags:
  - sysprog
  - network
  - news
---

Found some interesting progresses on io_uring. The zero-copy network
transmission with io_uring for TCP or UDP is ready for Linux networking. I also
agree that io_uring and eBPF will lead to the next era of Linux programming in
the near future.

- [Zero-copy network transmission with io_uring](https://lwn.net/Articles/879724/)
  - [Discussion on Hacker News](https://news.ycombinator.com/item?id=30144652)
- [Phoronix: IO_uring Zerocopy Send Is Ready For Linux 5.20 Networking](https://www.phoronix.com/news/Linux-5.20-IO_uring-ZC-Send)
- [Phoronix: Linux 6.6 Lands "Pretty Juicy" IOmap Improvements, Lower Latency With IO_uring](https://www.phoronix.com/news/Linux-6.6-IOmap-Improvements)
- [zero-copy RX for io_uring](https://lwn.net/Articles/913659/)

io_uring with another hot topic eBPF

- [How io_uring and eBPF Will Revolutionize Programming in Linux](https://www.scylladb.com/2020/05/05/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/)
  - [Discussion on Hacker News](https://news.ycombinator.com/item?id=25222243)
- [Cloudflare architecture and how BPF eats the world](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/)
  - [Discussion on Hacker News](https://news.ycombinator.com/item?id=19947970)
- [BPF meets io_uring](https://lwn.net/Articles/847951/)
- [BPF, XDP, Packet Filters and UDP](https://fly.io/blog/bpf-xdp-packet-filters-and-udp/)
  - [Discussion on Hacker News](https://news.ycombinator.com/item?id=24848391)

Resources on io_uring

- [RedHat Developers: Why you should use io_uring for network I/O](https://developers.redhat.com/articles/2023/04/12/why-you-should-use-iouring-network-io)
- [The Cloudflare Blog: Missing Manuals - io_uring worker pool](https://blog.cloudflare.com/missing-manuals-io_uring-worker-pool/)
- [Dank Wiki: IO uring](https://nick-black.com/dankwiki/index.php/Io_uring)
- [io_uring is not an event system](https://despairlabs.com/blog/posts/2021-06-16-io-uring-is-not-an-event-system/)
  - [Discussion on Hacker News](https://news.ycombinator.com/item?id=27540248)
- [io_uring is not (only) a generic asynchronous syscall facility](https://fancl20.github.io/contents/00-posts/2021-06-30-io_uring-is-not-only-a-generic-asynchronous-syscall-facility.html)
  - Computation happened closer to the hardware -
    [Toward decoupled system architecture](https://fancl20.github.io/contents/00-posts/2021-06-27-toward-decoupled-system-architecture.html)
- [Ringbahn: a safe, ergonomic API for io-uring in Rust](https://boats.gitlab.io/blog/post/ringbahn/)
- [A Universal I/O Abstraction for C++](https://cor3ntin.github.io/posts/iouring/)
- [A Programmer-Friendly I/O Abstraction Over io_uring and kqueue](https://tigerbeetle.com/blog/a-friendly-abstraction-over-iouring-and-kqueue/)
- [Adding io_uring to Java](https://korennoy.com/2023/06/09/adding-io_uring-to-java/)
