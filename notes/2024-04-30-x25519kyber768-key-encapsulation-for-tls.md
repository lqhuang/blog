---
title: X25519Kyber768 key encapsulation for TLS
date: 2024-04-30
tags:
  - news
  - cryptography
---

> Starting in Chrome 124, Chrome enables by default on all desktop platforms a
> new post-quantum secure TLS key encapsulation mechanism X25519Kyber768, based
> on a NIST standard (ML-KEM). [^chrome124]

Major browsers are starting to deliver post-quantum secure key exchange
mechanisms. Though the quantum threat is still far away, it's still essential to
migrate tls key agreements to prevent "store-and-decrypt" attack, which could be
able to decrypt stored traffic until a quantum computer is available in the
future.

But on the other side, the launch of Google Chrome 124 and Microsoft Edge 124
were appearently breaking TLS connections to some legacy web applications,
firewalls, and server products. Adoption of the new key exchange mechanism is a
long way to go.

Cloudflare have also made lots of effort to make the post-quantum cryptography
available to the public. They have tried to secure the connection from
Cloudflare to _origin_ servers in production from 2023 [^pq2origin]. Besides,
there is a tool [tldr.fail](https://tldr.fail) to help developer to show error
info with ClientHello messages during tls connection.

[^chrome124]: [Feature: X25519Kyber768 key encapsulation for TLS](https://chromestatus.com/feature/5257822742249472)
[^pq2origin]: [Cloudflare now uses post-quantum cryptography to talk to your origin server](https://blog.cloudflare.com/post-quantum-to-origins)

Other related posts:

- [Defending against future threats: Cloudflare goes post-quantum](https://blog.cloudflare.com/post-quantum-for-all)
- [The state of the post-quantum Internet](https://blog.cloudflare.com/pq-2024)
