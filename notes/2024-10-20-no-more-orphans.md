---
title: No More Orphans
date: 2024-10-20
tags:
  - scala
  - dev
src: https://blog.7mind.io/no-more-orphans
---

Recently, I read a blog post about the orphan[^no-more-orphans] import statement in Scala. It's quite interesting to read because I also have the same feeling about the import statement in Scala.

But I today I want to talk about another import statement feature in Scala.

Yeah, when starting with Scala, I really hate the import statement like `import cats.implicits._` or `import cats.syntax.all._` because it's not clear what's being imported.

I have to go to the documentation to confirm what's being imported. But unfortunately, the Scala community is also notorious for incomplete documentation and tutorials. So, I must go to the source code to know what's being imported.

Even after a while, I still don't understand or often **forget** what is being imported. I have to go back to the source code again and again.

And it's quite funny that they do things like this in tutorials. People come here to learn how to use the library, and they write `orphans` import statements assuming that the readers are already familiar with or experts in the library.

When you have a well-set-up IDE, you can just hover over the import statement and jump into source to see what's being imported. But what if I don't have a well-set-up IDE? And shouldn't we remember that high-level code is written for humans instead of for machines?

- I have to go to the source code to see what is being imported.
- I have to go to the source code to see what is being imported.
- I have to go to the source code to see what is being imported.

What I could accept is syntax or prelude import like `import cats.syntax.all.*` or `import cats.effect.prelude.*` for many feasible reasons:

And I strongly suggest libraries maintainers to declare what would happen while import above import statements. It should be not too hard to write a comment around the import statements.

> Explicit is better than implicit.
>
> -- Python Zen[^python-zen]

Eplicit import is a pretty code smell

[^no-more-orphans]: [No More Orphans](https://blog.7mind.io/no-more-orphans)
[^python-zen]: [The Zen of Python](https://peps.python.org/pep-0020/)
