---
title: 'Cheatsheet: Write Multiple Lines Content in YAML'
date: 2022-05-31
tags:
  - dev
  - til
---

It's crazy that there are NINE different ways to write multi-line strings in
YAML.

Here is a simple cheatsheet:

- Use `>` most of the time: interior line breaks are stripped out, although you
  get one at the end.
- Use `|` if you want those linebreaks to be preserved as `\n` (for instance,
  embedded markdown with paragraphs).
- Use `>-` or `|-` instead if you don't want a linebreak appended at the end.
- Use `"blahblah..."` if you need to split lines in the middle of words or want
  to literally type linebreaks as `\n`

And this is difference betweetn `"` and `'` in YAML:

| How to create a literal: | blank without quotes | `"`  | `'` |
| ------------------------ | -------------------- | ---- | --- |
| Single quote             | '                    | '    | ''  |
| Double quote             | "                    | `\"` | "   |
| Backslash                | \                    | `\\` | \   |

- Whenever applicable use the unquoted style since it is the most readable.
- Use the single-quoted style (`'`) if characters such as `"` and `\` are being
  used inside the string to avoid escpaing them and therefore improve
  readability.
- Use the double-quoted style (`"`) when the first two options aren't
  sufficient, i.e. in scenarios where more complex line breaks are required or
  non-printable characters are needed.

Check references for more detailed examples :(

> References:
>
> 1. [YAML Multiline](https://yaml-multiline.info/)
> 2. [How do I break a string in YAML over multiple lines?](https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines)
> 3. [YAML: Do I need quotes for strings in YAML?](https://stackoverflow.com/questions/19109912/yaml-do-i-need-quotes-for-strings-in-yaml)
