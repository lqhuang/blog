---
title: Google Python Style Guide
date: 2023-02-11
tags:
  - python
  - dev
---

许久不看 Google Python Style Guide, 里面推荐的 indentation 已经 2 spaces 改到 4
spaces 了 😅 还自己开发了 PyInk 补充 Black, 另外也随着 Python 引入的新功能更新了
一些有意思的内容 🤗

```python
class A:
    def foo(self, obj):
        match obj:
            case (1, a, 3):
                now_you_can_write_functions_or_codes()
            case C(x, y):
                ...
```

但是因为 Python 里 pattern matching 的语法过于~~优雅 ~~繁琐, 4 spaces 下随便写点
什么, 真正的逻辑代码就已经不知道缩进到哪里去了, 在 Python 里使用 2 spaces 好像我
又可以了...

> [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
