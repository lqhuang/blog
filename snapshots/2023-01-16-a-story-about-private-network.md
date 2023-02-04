---
title: A Story about Private Network Range
date: 2023-01-16
tags:
  - dev
  - til
---

```
export no_proxy=.local,.internal,.arpa,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
```

When I try to search the best pratice on setting `no_proxy`, I found an
interesting story about how the `192.168/16` subnet comes from LOL.

> @misterkbar:
>
> Unusure about `172...`, and `10....` seems rather obvious.
>
> `192.168...` is pretty funny though. It was originally Sun's network range.
> When they built Sun Workstations, they were all shipped with this address
> range in various config files. Since Sun started shipping product LONG before
> the Internet™ existed (the Arpanet™ did, but not the public Internet™), you
> could just use all these configuration files without modifying anything and
> BAM! Instant private network ( although back then, ALL networks were private
> :-) )... sort of like how the default printer for BSD Unix distributions was
> the machine in the basement of the UC Berkeley CS building!
>
> When Al Gore created the Information Superhighway, all of a sudden all these
> `192.168...` setups started conflicting. The answer was then obvious: place a
> NATing gateway on an installation and let `192.168...` be the private network.

References:

- [We need to talk: Can we standardize NO_PROXY?](https://about.gitlab.com/blog/2021/01/27/we-need-to-talk-no-proxy/)
- [Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
- [Why this private IP only range 172.16.0.0-172.31.255.255?](https://learningnetwork.cisco.com/s/question/0D53i00000Kt6C4CAJ/why-this-private-ip-only-range-1721600-17231255255-)
