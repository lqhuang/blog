---
title: Lean Scala (from Martin Odersky)
date: 2024-04-12
tags:
  - dev
  - scala
---

Last year, I post a
[snippet](./2023-05-07-another-two-cents-about-the-current-scala-situation.md)
for a thread discussed about current scala situation. And after multiple
releases and pretty good progressive adaption of scala 3, Martin Odersky, the
creator of Scala, declares his thoughts[^lean] about the future of Scala.
Although if you're active in the Scala community, Martin has been talking about
this for a while, it's still worth to follow/read. It's more like a formal
manifesto.

What is Lean Scala? Here are some key points:

- It should follow the Principle of Least Power.
  - Try to use the least powerful features first, only introduce black magic
    tricks when they are really needed.
- It should be immutable first, without being dogmatic about it.
  - As it says, prefer immutable data and pure functions, allow effects which
    are well contained and described. Scala team also plans to introduce
    **Capturing Types** to help with this.
- It should promote the core language over embedded DSLs.
  - Distinguish Lean Scala from "Scala as a host language for DSLs".
- It should focus on direct style.
  - Follow the last principle, Lean Scala should be direct and explicit. And
  - > Monadic effect systems shine in some areas but they are also a kind of
    > DSL, which creates specialized eco-systems and dialects.

Lean Scala looks like a good direction for Scala, especially for the new users
outside from FP world. Easy to learn, easy to use, easy to maintain would make a
language live longer 🥹 and be adapted by more real cases.

Then how could we promote Lean Scala? Martin suggests: 1. Write technical
documentation; 2. Work on tooling support; 3. Encourage efforts to assemble and
promote library stacks. Every language won't be prosperous without its community
and eco-system.

For me, I'm still a fan of Scala, and I'm glad to see the progress of Scala 3
which I thought is really underrated.

Refs:

[^lean]: [Lean Scala](https://odersky.github.io/blog/2024-04-11-post.html)
