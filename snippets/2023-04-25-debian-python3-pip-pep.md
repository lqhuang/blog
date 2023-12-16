---
title: Debian's Python Distribution Introduces PEP 668 support

date: 2023-04-25
tags:
  - python
  - dev
---

What's a good news! DO NOT touch default Python installed by OS, it's always
considered as a bad practice on the flip side.

> Debian's python3.11 interpreter will soon (>= 3.11.2-3) declare the
> installation to be EXTERNALLY-MANAGED, instructing pip to disallow package
> installation outside virtualenvs.
>
> Practically, this means that you can't use pip to install packages outside a
> virtualenv, on Debian's Python interpreter by default, any more.

Or you could use third python env managers like Pyenv, Conda or other similars.

Refs:

- [PEP 668 – Marking Python base environments as "externally managed"](https://peps.python.org/pep-0668/)
- [Update NEWS to reflect the true PEP-668 rollout in cpython3](https://salsa.debian.org/python-team/packages/python-pip/-/blob/315bcd6f4cdb5bcfb8a74f1e599739cc74c86432/debian/NEWS)
