---
title: Picture with theme support in GitHub Flavored Markdown
date: 2024-12-01
tags:
  - github
  - dev
  - til
---

TIL, GitHub Flavored Markdown supports specifying the theme an image is shown to[^themed-picture]. This is useful when you want to show different images distinguish between light and dark color modes.

An old method using a fragment appended to the URL (`#gh-dark-mode-only` or `#gh-light-mode-only`) to specify images based on the theme is deprecated in favor of the `prefers-color-scheme` media query which also a standard html element.

```html
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png
    "
  />
  <img
    alt="Shows an illustrated sun in light mode and a moon with stars in dark mode."
    src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png"
  />
</picture>
```

the above code displays a sun image for light themes and a moon for dark themes, as shown below:

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png
    "
  />
  <img
    alt="Shows an illustrated sun in light mode and a moon with stars in dark mode."
    src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png"
  />
</picture>

[^themed-picture]: [Basic writing and formatting syntax - Specifying the theme an image is shown to](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#specifying-the-theme-an-image-is-shown-to)
