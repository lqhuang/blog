---
title: Google Python Style Guide
date: 2023-02-11
tags:
  - python
  - dev
---

许久不看 Google Python Style, 里面的 indentation 已经 2 spaces 改到 4 spaces 了
😅 还有也随着 Python 引入的 new features 更新了一些有意思的内容 🤗

```python
def foo():
    match obj:
        case (1, a, 3):
            blablah
        case C(x, y):
            blablah
```

但是随着 pattern matching 的语法过于~~繁琐 ~~, 4 spaces 下随便写点什么, 真正的逻
辑代码就已经不知道锁进到哪里去了... 2 spaces 好像又可以了...

> [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
