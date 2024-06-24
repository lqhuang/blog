---
title: Link Issues by Keyword of Commit Message
date: 2024-02-14
tags:
  - dev
  - git
---

I just knew that you can link a pull request to an issue by using a supported
**keyword** in the pull request's description or in a commit message on GitHub.

- close
- closes
- closed
- fix
- fixes
- fixed
- resolve
- resolves
- resolved

For example, a commit message with the text `Fix #32` would close issue 32
automatically.

If you use a keyword to reference a pull request comment in another pull
request, the pull requests will be linked. Merging the referencing pull request
also closes the referenced pull request.

The syntax for closing keywords depends on whether the issue is in the same
repository as the pull request.

Refs:

- [GitHub Docs: Linking a pull request to an issue using a keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
