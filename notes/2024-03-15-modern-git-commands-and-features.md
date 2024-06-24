---
title: Modern Git Commands and Features You Should Be Using
date: 2024-03-15
tags:
  - git
  - dev
---

I always like to find somethings in modern ways 🥰 Here are serveral new
features for Git. My short notes:

- `git switch` and `git restore` are new commands that are more intuitive than
  `git checkout` and `git reset`. They are also safer, as they don't change the
  working directory by default.
- `git sparse-checkout` is a new feature that allows you to only checkout the
  parts of the repository you need. This is useful for large repositories or
  monorepo style env.
- `git worktree` is a new feature that allows you to have multiple working
  directories for the same repository. This command allows us to have multiple
  branches of the same repository checked out at the same time.
- `git bisect` is a command that helps you find the commit that introduced a
  bug. It's been around for a while, but it's not used as often as it should be.

Refs:

- [Modern Git Commands and Features You Should Be Using](https://martinheinz.dev/blog/109)
