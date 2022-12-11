---
title: daemon - Writing and packaging system daemons
date: 2022-10-30
tags:
  - good-reading
  - dev
---

In the past days, I always confused why I need to activate a `.socket` daemon
like `systemd enable --now xxx.socket` instead of `.service`.

> **Socket-Based Activation**: In order to maximize the possible parallelization
> and robustness and simplify configuration and development, it is recommended
> for all new-style daemons that communicate via listening sockets to employ
> socket-based activation.
>
> Ref:
> [daemon(7) — Linux manual page](https://man7.org/linux/man-pages/man7/daemon.7.html)
