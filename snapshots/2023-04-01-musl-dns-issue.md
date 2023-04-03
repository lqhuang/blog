---
title: DNS Query Issue in Apline Image with MUSL libc
date: 2023-04-01
tags:
  - dev
  - til
---

Until now I just know there're DNS issues in Apline image, which is major caused
by musl libc. Check
[Racy conntrack and DNS lookup timeouts](https://www.weave.works/blog/racy-conntrack-and-dns-lookup-timeouts)

All right, I know musl libc is different to gnu libc, usually user shouldn't
feel differences in app level, but this definitely an user-aware issue.

> 1. glibc could be configured to send those requests sequentially, with
>    `single-request` and `single-request-reopen` options, but musl cannot.
>
> 2. musl's resolver previously did not support the "domain" and "search"
>    keywords in `resolv.conf`. This feature was added in version 1.1.13, but
>    its behavior differs slightly from glibc's

The good news is query DNS sequentially is not the only one solution for
netfilter race problem (UDP query would be dropped accidentally).

Refs:

- [Functional differences from glibc - Name Resolver/DNS](https://wiki.musl-libc.org/functional-differences-from-glibc.html)
- [Why does musl make my Rust code so slow?](https://andygrove.io/2020/05/why-musl-extremely-slow)
- [如何解决 Kubernetes 的 DNS 延迟问题 (Chinese)](https://feisky.xyz/posts/2020-04-09-dns-latency)
- [记一次 k3s 的 dns 问题调查解决过程 (Chinese)](https://www.liuquanhao.com/posts/%E8%AE%B0%E4%B8%80%E6%AC%A1k3s%E7%9A%84dns%E9%97%AE%E9%A2%98%E8%B0%83%E6%9F%A5%E8%A7%A3%E5%86%B3%E8%BF%87%E7%A8%8B/)
- [Using NodeLocal DNSCache in Kubernetes Clusters](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns)
- [Wener Wiki - musl (Chinese)](https://wener.me/notes/os/linux/lib/musl)
