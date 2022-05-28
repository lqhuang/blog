---
title: "BooK: HTTP/3 Explained"
date: 2019-12-13
tags:
  - network
  - book
---

Welcome to next stage of HTTP!

What is HTTP/3?

- QUIC (Quick UDP Internet Connections) is a secure transport protocol allows
  the fast and easy sending of simple packets over the connection-less UDP
- HTTP/3 == HTTP/2 over QUIC

Key advantages of QUIC over TCP+TLS+HTTP2 include:

- Improved connection establishment speed (0-rtt).
- Improved congestion control by moving congestion control algorithms into the
  user space at both endpoints.
- Improved bandwidth estimation in each direction to avoid congestion.
- Improved multiplexing without head-of-line blocking.
- Contains forward error correction (FEC).

Challenges:

- ISP often filters UDP packets for QoS

_HTTP/3 Explained_ is such a good reading materials to understand this new
protocol.

> [QUIC: What is behind the experimental Google Protocol?](https://www.ionos.com/digitalguide/hosting/technical-matters/quic-the-internet-transport-protocol-based-on-udp)
>
> [HTTP/3 Explained](https://http3-explained.haxx.se)
>
> [HTTP/3 Explained - 简体中文](https://http3-explained.haxx.se/zh)
>
> [What is HTTP/2 – The Ultimate Guide](https://kinsta.com/learn/what-is-http2)
>
> Updated (May 28, 2022): Add some quotes from
> [quinn-rs/quinn](https://quinn-rs.github.io/quinn/networking-introduction.html)
