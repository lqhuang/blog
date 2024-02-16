---
title: Multi-Database Support in DuckDB
date: 2024-02-12
tags:
  - news
  - database
---

> TL,DR: DuckDB can attach MySQL, Postgres, and SQLite databases in addition to
> databases stored in its own format. This allows data to be read into DuckDB
> and moved between these systems in a convenient manner.

Using the SQLite extension, we can open a SQLite database file and query it as
we would query a DuckDB database.

```sql
ATTACH 'sakila.db' AS sakila (TYPE sqlite);
SELECT title, release_year, length FROM sakila.film LIMIT 5;
```

This is insane!

```sql
ATTACH 'sqlite:sakila.db' AS sqlite;
ATTACH 'postgres:dbname=postgresscanner' AS postgres;
ATTACH 'mysql:user=root database=mysqlscanner' AS mysql;
```

In modern data analysis, data definitely is combined from a wide variety of
different sources. What a game changer feature.

Ref:

- [Multi-Database Support in DuckDB](https://duckdb.org/2024/01/26/multi-database-support-in-duckdb.html)
