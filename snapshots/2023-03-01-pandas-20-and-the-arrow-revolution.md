---
title: Pandas 2.0 and the Arrow revolution
date: 2023-03-01
tags:
  - python
  - news
---

Pandas 2.0 with new Arrow backend shows significantly performance improvements
on various operations.

Apache Arrow (including arrow flight) is eating the data science and OLAP world:
Pandas, Polars, DuckDB, Influx-iox, Databend ...

> All problems in computer science can be solved by another level of indirection
> --- Butler Lampson

One intersting point is in the future container construction or transformation
among Pandas, Polar and DuckDB would become cheaper or zero-copy due to they
could share the same low-level data types and memory layout.

Refs:

- [Pandas 2.0 and the Arrow revolution (part I)](https://datapythonista.me/blog/pandas-20-and-the-arrow-revolution-part-i)
- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals)
- [Debatable benchmark from from Ritchie Vink](https://twitter.com/RitchieVink/status/1632334005264580608)
<!-- - [Pandas 2.0 and the Arrow revolution (part II)](https://datapythonista.me/blog/pandas-20-and-the-arrow-revolution-part-ii) -->

Updated: 2023-04-20

- [Pandas 2.0 vs Pandas 1.3 — Performance Comparison](https://medium.com/@santiagobasulto/pandas-2-0-performance-comparison-3f56b4719f58)
