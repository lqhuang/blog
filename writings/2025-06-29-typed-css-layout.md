---
title: 'Typed CSS Layout in React with TypeScript'
created: 2025-06-29
updated: 2025-10-29
draft: true
tags:
  - web
  - design
  - typescript
---

太累了 😭

not a pro Front end eng

not like vibe coding

tailwindcss v4

radix-theme/layout

is great

but

class consider harmfull

parcel

the good news is

I use TypeScript and only use TypeScript

https://github.com/adobe/react-spectrum/blob/main/packages/%40react-spectrum/s2/src/style-utils.ts

但是这个文件的东西都没有导出 ...

```ts
const allowedOverrides = [
  'margin',
  'marginStart',
  'marginEnd',
  'marginTop',
  'marginBottom',
  'marginX',
  'marginY',
  'flexGrow',
  'flexShrink',
  'flexBasis',
  'justifySelf',
  'alignSelf',
  'order',
  'gridArea',
  'gridRowStart',
  'gridRowEnd',
  'gridColumnStart',
  'gridColumnEnd',
  'position',
  'zIndex',
  'top',
  'bottom',
  'inset',
  'insetX',
  'insetY',
  'insetStart',
  'insetEnd',
] as const
```

```ts
export type StylesProp = StyleString<
  (typeof allowedOverrides)[number] | (typeof widthProperties)[number]
>
export type StylesPropWithHeight = StyleString<
  | (typeof allowedOverrides)[number]
  | (typeof widthProperties)[number]
  | (typeof heightProperties)[number]
>
export type StylesPropWithoutWidth = StyleString<
  (typeof allowedOverrides)[number]
>
```

Components are great ... but ...

Sep 10, 2025

I deprecated all Tailwind CSS in my personal project

他更像是我的一个学习成果

## Main components decisi

### Why react-aria

I don't won't reinvent everything now

I'm just reinventing design system

If you think your "business" or "project" will bigger than Adobe.

Than great just keep your way

### Why not pigment

a minimum runtime is acceptible

it may not the best, it would be the optimal
