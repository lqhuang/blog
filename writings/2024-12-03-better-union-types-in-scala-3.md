---
title: Better Union Types in Scala 3
created: 2024-12-03
updated: 2024-12-03
tags:
  - scala
  - functional-programming
draft: true
---

When I was working on a Scala project (I havn't experence the era before Scala 2.12 too much, I learn it from 2.13 and ship to 3 fastly), I found that I was confused about the use of `sealed` to implement Union types in Scala.

在 Scala 中利用 `sealed` 来实现 Union types 是否违反了里式替换原则 (Liskov Substitution Principle, LSP)？

在 scala 3 以前, 并没有正式地支持 `|` 语法来定义一个 Union type. 但是可以通过 `sealed trait` / `sealed class` 来实现类似的效果.

```scala
sealed trait A

case class B() extends A
case class C() extends A

type D = B | C
```

但是这样的定义会违反 LSP, 因为 `A` 是 `B` 和 `C` 的父类, `A != B | C`.

> @duhace: Scala does support Union types. You can use shapeless to work with them right now because rolling your own true Union types is a form of black magic right now. Here's the basic technique for them: http://milessabin.com/blog/2011/06/09/scala-union-types-curry-howard/

> [deleted]: Scala does not have sum (discriminated union) types.
>
> scalaz, Shapeless, and Cats all have very powerful encodings of them, as "Coproducts," because sums are the categorical dual of products. I've worked quite a bit with Shapeless' `Coproduct`, so if you have any questions, please ask away!

`sealed` 的本意是为了防止从其他文件 (或者称为外部) 扩展这个 trait. 这样做的目的是为了避免在其他文件中定义新的子类, 从而破坏子类的完整性导致无法进行模式匹配的 exhaustive check.

模式匹配并不是在完全地做 Union types 的匹配, 在匹配 sealed class 的时候, 是在匹配所有的子类. 这样做的目的是为了保证模式匹配的完整性.

这样实现的 "Union Types" 不是真正的 Union Types

这个问题并不涉及 nominal typing 和 structural typing. 当然社区也对如何让 Scala 3 (Dotty) 的 True Union Types 更好用有很多的讨论甚至是改进

- [Everything You Ever Wanted to Know About Sealed Traits in Scala](https://underscore.io/blog/posts/2015/06/02/everything-about-sealed.html)

- [Any recommendations on how to get a union type in Scala?](https://www.reddit.com/r/scala/comments/funb0c/any_recommendations_on_how_to_get_a_union_type_in/)
- [Union types in Scala](https://www.reddit.com/r/scala/comments/4g43js/union_types_in_scala/)

- [Beyond Liskov: Type Safe Equality in Scala](https://www.lihaoyi.com/post/BeyondLiskovTypeSafeEqualityinScala.html)
- [Do sealed/final classes in C#/Java violate the open/closed principle?](https://www.quora.com/Do-sealed-final-classes-in-C-Java-violate-the-open-closed-principle)
- [Should a class know about its subclasses?](https://softwareengineering.stackexchange.com/questions/219543/should-a-class-know-about-its-subclasses)
- [The point of sealing a class](https://softwareengineering.stackexchange.com/questions/415501/the-point-of-sealing-a-class)

本质上确实像是早期的时候为了向 Java 妥协, 实现的类 Union Types 的语法糖 (其他的妥协比如 Scala 2 以前的顶类型和底类型是错的, 反过来了). 社区里也有过讨论, 要把 sealed 扩展到其他文件来实现 ADT (union types / sum types).

- [Illegal inheritance from sealed class Type](https://users.scala-lang.org/t/illegal-inheritance-from-sealed-class-type/6888/)
- [Enabling sealed traits across different files with union type desugaring](https://contributors.scala-lang.org/t/enabling-sealed-traits-across-different-files-with-union-type-desugaring/6040)

- [Making union types even more useful](https://contributors.scala-lang.org/t/making-union-types-even-more-useful/4927)
  - [True union types #1550](https://github.com/scala/scala3/pull/1550)
  - [Make type inference preserve user-written union types with more than two members to infer a more precise type than Matchable #11449](https://github.com/scala/scala3/issues/11449)

或者说把 sealed 理解成 union type 或者 ADT ... 本身就是错的 (但是主要随便一搜 Scala union types, 大部分都会说利用 sealed blablabla .... 逃)

And we also have `enum` in Scala 3 now.

但是确实 Scala 还是一直是个 JVM first 的语言, 所以很多设计都是为了向 Java 妥协. 但是 Scala 3 也在不断地改进, 比如 union types 的支持, 比如 inline 的支持等等.

在讨论如何优化 Scala 3 的 Union types 的时候, commetee member 的第一反应是在 JVM 上实现这个问题的 trade off 而不是本身带给用户或者社区的价值.

我当然希望 Scala 3 成为一个更好的语言, 不仅仅是一个 Java 的替代品. not a better Java, not a better Haskell, not a better Python (what I'm working on), but a better Scala. Cheers!
