---
title: "JSON isn't JSON"
date: 2025-10-08
tags:
  - dev
  - good-reading
---

> JSON (JavaScript Object Notation) was supposed to be the universal data interchange format that would solve the compatibility nightmares of XML. What looks like astraightforward data format becomes a minefield of subtle incompatibilities, edge cases, and implementation quirks that can break your applications in unexpected ways.[^ref]

Common pitfalls (selected by myself from the article):

- The Number Nightmare
  - not only precision loss for large integers
  - but also `NaN` and `Inf`, see also Daniel Lemire's tweet [^daniel]
- String Encoding Chaos
  - The character `é` can be represented as:
    - A single codepoint: `U+00E9` (`é`)
    - Composed form: `U+0065 U+0301` (`e` + ` ́`)
- Object Key Ordering
  - It's fun that this may influence LLM KV cache performance now
- Null vs. Undefined vs. Missing
- Date and Time Fun

Authors' Recommendations:

- Use Schema Validation: The First Law of JSON Robotics
- Normalize Data Types
- Library Selection Matters
- Test Cross-Language Compatibility

> May the Parse Be With You

[^ref]: [JSON is not JSON Across Languages | Dochia CLI Blog](https://blog.dochia.dev/blog/json-isnt-json/):
[^daniel]: [@lemire: The JSON format requires numbers to be actual numbers: Inf and NaN are not accepted.](https://x.com/lemire/status/1950714238617469118)
