---
title: Caddy 2.5.0 Upgrade Issues
date: 2022-05-01
tags:
  - dev
  - news
---

If you put your servers behind CDN like Cloudflare or Caddy is not reaced
firstly, there are serveral notable changes while updating Caddy to 2.5.0:

> ⚠️ Reverse proxy: Incoming `X-Forwarded-*` headers will no longer be
> automatically trusted, to prevent spoofing. **Now, `trusted_proxies` must be
> configured to specify a list of downstream proxies which are trusted to have
> sent good values.** You only need to configure trusted proxies if Caddy is not
> the first server being connected to. For example, if you have Cloudflare in
> front of Caddy, then you should configure this with Cloudflare's
> [list of IP ranges](https://www.cloudflare.com/en-ca/ips/).

References:

1. <https://github.com/caddyserver/caddy/releases/tag/v2.5.0>
2. <https://caddyserver.com/docs/caddyfile/directives/reverse_proxy>
3. <https://caddy.community/t/caddy-v2-5-0-rc-1-and-x-forwarded-headers/15694>
4. <https://blog.hlyue.com/2021/12/01/cloudflare-caddy-mutual-TLS>
5. <https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull>
