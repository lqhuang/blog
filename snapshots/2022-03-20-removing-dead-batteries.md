---
title: "Removing dead batteries from the standard library"
date: 2022-03-20
tags:
  - python
  - news
---

Python has famous "batteries included" philosophy for its rich standard library
modules, but there are lots of modules have been oudated or inactive for past
years. With acceptance of [PEP 594], serveral modules will be marked as
`DeprecationWarning` from Python 3.11 and be removed from Python 3.13, and
Python on mobile platforms like `BeeWare` or `WebAssembly` (e.g. pyodide) also
will benefit from reduced download size.

Part of proposed modules: `cgi`, `crypt`, `smtpd`, `telnetlib`, ...

> [PEP 594 – Removing dead batteries from the standard library](https://peps.python.org/pep-0594/)
