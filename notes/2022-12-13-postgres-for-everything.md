---
title: Just Use Postgres for Everything -- how to reduce complexity and move faster
date: 2022-12-13
tags:
  - dev
---

This's why I always love Postgres in small scale projects.

> - Use Postgres for caching instead of Redis with UNLOGGED tables and TEXT as a
>   JSON data type. Use stored procedures to add and enforce an expiry date for
>   the data just like in Redis.
> - Use Postgres as a message queue with SKIP LOCKED instead of Kafka (if you
>   only need a message queue).
> - Use Postgres with Timescale as a data warehouse.
> - Use Postgres with JSONB to store Json documents in a database, search and
>   index them - instead of Mongo.
> - Use Postgres as a cron demon to take actions at certain times, like sending
>   mails, with pg_cron adding events to a message queue.
> - Use Postgres for Geospacial queries.
> - Use Postgres for Fulltext Search instead of Elastic.
> - Use Postgres to generate JSON in the database, write no server side code and
>   directly give it to the API.
> - Use Postgres with a GraphQL adapter to deliver GraphQL if needed.
>
> There I've said it, just use Postgres for everything.
>
> -- Stephan Schmidt

Src: [Just Use Postgres for Everything ](https://www.amazingcto.com/postgres-for-everything/)
