---
title: Logging and Testing Tips in Python
date: 2022-07-02
tags:
  - python
---

Recent good readings in Python logging and testing:

[Logging in Python like a PRO 🐍🌴](https://guicommits.com/how-to-log-in-python-like-a-pro/)

![](https://docs.monadical.com/uploads/5fb79fe51e47ca767ab94b61e.png 'from [Credit to Monadical blog](https://monadical.com/posts/ins-and-outs-of-logging-in-python-part-one.html)')

| Level      | When it's used                                                                                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`    | Detailed information, typically of interest only when diagnosing problems.                                                                                             |
| `INFO`     | Confirmation that things are working as expected.                                                                                                                      |
| `WARNING`  | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low'). The software is still working as expected. |
| `ERROR`    | Due to a more serious problem, the software has not been able to perform some function.                                                                                |
| `CRITICAL` | A serious error, indicating that the program itself may be unable to continue running.                                                                                 |

With primer tutorials from Python std library
[Logging HOWTO](https://docs.python.org/3/howto/logging.html) and
[Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html), these
are enough to get through to Python logging.

Testing:

- [My Python testing style guide](https://blog.thea.codes/my-python-testing-style-guide)
- ["Don't Mock What You Don't Own" in 5 Minutes](https://hynek.me/articles/what-to-mock-in-5-mins)
