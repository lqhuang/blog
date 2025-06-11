---
title: New Named Tuples Feature since Scala 3.7
date: 2025-04-11
tags:
  - scala
  - til
src: https://scala-lang.org/api/3.x/docs/docs/reference/experimental/named-tuples.html
---

Just know Scala 3.7 will introduce Named Tuples. Interesting features. And I found the proposal is drafted at Jan 13, 2024.

```scala
type Person = (name: String, age: Int)
val Bob: Person = (name = "Bob", age = 33)

Bob match
  case (name, age) => println(s"$name is $age years old")

val persons: List[Person] = ...
val minors = persons.filter: p => p.age < 18
```

> **Structural Types**
>
> We also considered to expand structural types. Structural types allow to abstract over existing classes, but require reflection or some other library-provided mechanism for element access. By contrast, named tuples have a separate representation as tuples, which can be manipulated directly. Since elements are ordered, traversals can be defined, and this allows the definition of type generic algorithms over named tuples. Structural types don't allow such generic algorithms directly. Be could define mappings between structural types and named tuples, which could be used to implement such algorithms. These mappings would certainly become simpler if they map to/from named tuples than if they had to map to/from user-defined "HMap"s.
>
> By contrast to named tuples, structural types are unordered and have width subtyping. This comes with the price that no natural element ordering exist, and that one usually needs some kind of dictionary structure for access. We believe that the following advantages of named tuples over structural types outweigh the loss of subtyping flexibility:
>
> - Better integration since named tuples and normal tuples share the same representation.
> - Better efficiency, since no dictionary is needed.
> - Natural traversal order allows the formulation of generic algorithms such as projections and joins.
>
> **Conformance**
>
> ...
>
> Looking at precedent in other languages it feels like we we do want some sort of subtyping for easy convertibility and an implicit conversion in the other direction. This proposal picks `unnamed <: named` for the subtyping and `named -> unnamed` for the conversion.
>
> ...

Refs:

- [Scala 3 Reference - Experimental Named Tuples](https://scala-lang.org/api/3.x/docs/docs/reference/experimental/named-tuples.html)
- [Going structural with Named Tuples by Jamie Thompson | Scalar Conference 2025](https://youtu.be/Qeavi9M65Qw)
- [SIP-58 - Named Tuples](https://docs.scala-lang.org/sips/named-tuples.html)
