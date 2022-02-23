---
title: "在 FlatPages 下启用 Markdown 的 LaTex 数学公式支持"
created: 2016-12-29
updated: 2016-12-29
tags: ["flask", "mathjax"]
---

Markdown 下的 LaTex 数学公式支持

作为一个理科生，一直想要在 Markdown 下使用 LaTex 数学公式。自己的博客用的是 Flask 的 FlatPages，网上查了一圈都没有现成的方案，差点就想造轮子了。幸好发现 FlatPages 用的是 Python-Markdown 来渲染`md`格式到`html`，这下就好办多了，Python-Markdown 支持第三方的扩展，也已经比较成熟了。

在 Python-Markdown 的 [Github wiki](https://github.com/waylan/Python-Markdown/wiki/Third-Party-Extensions) 上有各种第三方扩展的介绍，可以看到支持 Math/LaTex 的扩展还是很多的，但是我简单翻了一下，实现的办法都不太一样，并且使用方式也不一样，出于轻量化的原因，我更喜欢最简单的方式实现 LaTex 的公式支持，我看中了`mdx_math`和`python-markdown-math`这两个，其中`mdx_math`的包都已经 3~5 年没更新了，而且尝试了下了无法在 Python 3 下使用，由于代码比较简单，甚至产生了想改成 Python 3 支持的扩展。不过最后还是觉得不浪费这个时间了。`python-markdown-math`是调用了了 MathJax 的 API，也算是比较成熟的实现了，并且可以通过 PyPI 来安装，但是要新加一个 JS 的连接，对于不断膨胀的 JS 库，总是觉得不够 KISS(Keep It Stupid Simple) 哈哈哈。

使用`python-markdown-math`也非常的简单，具体的说明在其[github 主页](https://github.com/mitya57/python-markdown-math)上也有，安装完以后只要在 FlatPages 的 config 文件中加上`FLATPAGES_MARKDOWN_EXTENSIONS = ['mdx_math']`即可（记得在模板中加载 MathJax 的 JS 文件）

本文也作为一个显示效果的测试。

python-markdown-math 调用的是 MathJax 的 API，所以 LaTex 公式的输入也按照 MathJax 的方式来定义。

MathJax 支持行内公式 (inline) 和独立公式 (stand alone)，行内公式的可以用 `\(...\)` 来表示，行间公式可以用 `$$...$$`, `\[...\]` 和 `\begin{ }\end`。可以注意到的是默认的设置里面是无法用 `$...$` 来表示行间公式，这和通常的 LaTex 习惯不相符，可能需要适应一下。MathJax 给出的理由是 `$` 分隔符是个常见的标识符，例如在 Markdown 中出现 "... the cost is $2.50 for the first one, and $2.00 for each additional one ..." 就会无无法处理，因次默认关闭了 `$\` 作为 LaTex 公式的标记。但是可以通过两种办法开启 `$` 标识符的使用，一种是在 Python 的 Markdown extension 中通过传递 `enable_dollar_delimiter=True` 的配置，二是直接在 MathJax 的 JS [配置](http://docs.mathjax.org/en/latest/start.html) 中进行设置，这两种方式在各自的文档中都有说明。

下面是一些测试:

行内(inline)模式`\(...\)`: \(\alpha, \beta, \gamma\), \(\Omega\), \(\pi\).

独立(stand alone)模式:

`$$...$$`:

$$ax^2 + bx + c = 0$$

`\[\]`:

\[x = {-b \pm \sqrt{b^2-4ac} \over 2a}.\]

`\begin{}\end`(不成功):

\begin e^{\pi i} + 1 = 0 \end

---

PS: 额外发现发现加入公式以后，中文页面下的排版非常的不美观、无法实现中文的两端对齐。经过搜索后，发现有[汉字标准格式](https://hanzi.pro/)的排版框架

    <link href="//cdn.bootcss.com/Han/3.3.0/han.min.css" rel="stylesheet">
    <script src="//cdn.bootcss.com/Han/3.3.0/han.min.js"></script>

但是目前经过尝试后还是暂时无法使用(在 blog 界面卡死)。挖了一个大坑，等待填坑......
