---
title: Your API Shouldn't Redirect HTTP to HTTPS
date: 2024-06-11
tags:
  - dev
  - security
---

@jviide wrote a blog post[^http-redirects] about why your API shouldn't redirect
HTTP to HTTPS. He is right. It's probably a bad practice to simply redirect
without any other notification. Your secrets could already be leaked while
you're accessing the HTTP endpoint. So, what does the author suggest to do?

1. Make the failure visible to the user or caller.
2. Revoke API keys and tokens send over the unencrypted connection.

[^http-redirects]:
    [Your API Shouldn't Redirect HTTP to HTTPS](https://jviide.iki.fi/http-redirects)
