---
title: "GitHub Introduces New Alerts Syntax"
date: 2023-08-27
tags:
  - dev
  - news
  - til
---

I just check the GFM (Github Flavored Markdown) spec to confirm the latest alert
syntax which you probably have knew yet from other sources.

> On GitHub, they are displayed with distinctive colors and icons to indicate
> the significance of the content.
>
> To add an alert, use a special blockquote line specifying the alert type,
> followed by the alert information in a standard blockquote. Five types of
> alerts are available:
>
> ```markdown
> > [!NOTE] Useful information that users should know, even when skimming
> > content.
>
> > [!TIP] Helpful advice for doing things better or more easily.
>
> > [!IMPORTANT] Key information users need to know to achieve their goal.
>
> > [!WARNING] Urgent info that needs immediate user attention to avoid
> > problems.
>
> > [!CAUTION] Advises about risks or negative outcomes of certain actions.
> ```

Besides that, the first time I know GFM could also render colors automatically!
What's more ✨, it supports multiple color models:

- HEX: `#0969DA`
- RGB: `rgb(9, 105, 218)`
- HSL: `hsl(212, 92%, 45%)`

References:

1. [GitHub Docs - Basic writing and formatting syntax: Alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
2. [GitHub Docs - Basic writing and formatting syntax: Supported Color Models](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#supported-color-models)
