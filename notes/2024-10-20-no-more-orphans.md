---
title: No More Orphans
date: 2024-10-20
tags:
  - scala
  - dev
src: https://blog.7mind.io/no-more-orphans
---

Recently, I read a blog post about the orphan[^no-more-orphans] import statement in Scala. It's quite interesting to read because I also have the same feeling about the import statement in Scala.

But I today I want to talk about the import statement in Scala.

Yeah, when starting with Scala, I really hate the import statement like `import cats.implicits._` or `import cats.syntax.all._` because it's not clear what they are importing. I have to go to the documentation to see what they are importing.

But unfortunately, Scala community is also notorious for incomplete documentations and tutourials. So, I have to go to the source code to see what they are importing.

Even after a while, I still don't understand what they are importing. I have to go to the source code to see what they are importing.

And it's quite funny that do things like this in tutorials. People come here to learn how to use, and you write `orphans` import statement to assume that they know that they are familiar or an expert with the library.

When you have a well setup IDE, you can just hover over the import statement to see what they are importing. But I don't have a well setup IDE. I use Vim and Coc.nvim. I have to go to the source code to see what they are importing.

- I have to go to the source code to see what they are importing.
- I have to go to the source code to see what they are importing.
- I have to go to the source code to see what they are importing.

What I only accept is implcit or prelude import like `import cats._` or `import cats.effect._` because they are clear what they are importing.

And I strongly suggest libraries maintainers to write what would happen while import above import statement. It's not hard to write a comment above the import statement.

Eplicit import is a pretty code smell like Python Zen[^python-zen] says:

```
Explicit is better than implicit.
```

[^no-more-orphans]: [No More Orphans](https://blog.7mind.io/no-more-orphans)
[^python-zen]: [The Zen of Python](https://peps.python.org/pep-0020/)
