---
title: Pointer as a Type or Different Roles of the Asterisk in Clang
date: 2023-12-02
tags:
  - clang
  - discussion
---

Which style do you prefer to declare a variable in C?

1. `int *name`
2. `int* name`

Rasmus Andersson (@rsms) open a thread [^src] in [X](https://x.com) to discuss
the history of the convention of put asterisk symbol (`*`) (also known as unary
operator) as a pointer type attched to the name (style 1) rather than the type
(style 2).

Nowadays, after a few years of experience as a programmer, I prefer style 2.
It's more practical and easier to read in the functional programming way.

There are also many quite interesting comments and supplementary materials in
the thread about deferencing operator [^rsms][^so][^dpc_pw], historical
choices [^bell] and personal flavor [^stroustrup]. Worth to dig in.

Only one critical warning to pick the second style

> Avoid declaring more than one variable per statement! -- Phil Eaton
> (@eatonphil) [^eaton]

That means DO

```c
int* foo;
int* bar;
```

and DO NOT

```c
int* foo, bar;
```

[^src]: [Origin thread from @rsms](https://twitter.com/rsms/status/1730466033897730550)
[^eaton]: [Comment from @eatonphil](https://twitter.com/eatonphil/status/1730549092239978794)
[^rsms]: [Comment from @rsms](https://twitter.com/rsms/status/1730478285208105062)
[^so]: [StackOverflow - How to explain C pointers (declaration vs. unary operators) to a beginner?](https://stackoverflow.com/questions/27484168/how-to-explain-c-pointers-declaration-vs-unary-operators-to-a-beginner)
[^bell]: [Bell Labs - The Development of the C Language](https://www.bell-labs.com/usr/dmr/www/chist.html)
[^dpc_pw]: [Comments from @dpc_pw](https://twitter.com/dpc_pw/status/1730833771359011319)
[^stroustrup]: [Bjarne Stroustrup's C++ Style and Technique FAQ - Is `int* p;` right or is `int *p;` right?](https://www.stroustrup.com/bs_faq2.html#whitespace)
