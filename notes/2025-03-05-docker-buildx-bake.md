---
title: Docker Bake is Now Generally Available
date: 2025-03-05
tags:
  - dev
  - container
  - news
---

Docker announced that Docker Bake is now generally available[^1]. Docker Bake is an orchestration tool that streamlines Docker builds.

It help developers to transform complex build commands into declarative style configurations, which means from [^2]

```console
$ docker build \
    -f Dockerfile \
    -t myapp:latest \
    --build-arg foo=bar \
    --no-cache \
    --platform linux/amd64,linux/arm64 \
    .
```

to

```hcl
target "myapp" {
  context = "."
  dockerfile = "Dockerfile"
  tags = ["myapp:latest"]
  args = {
    foo = "bar"
  }
  no-cache = true
  platforms = ["linux/amd64", "linux/arm64"]
}
```

> You can write Bake files in HCL, YAML (Docker Compose files), or JSON. In general, HCL is the most expressive and flexible format, which is why you'll see it used in most of the examples in this documentation, and in projects that use Bake.
>
> (Well, I may don't think so =.=)

[^1]: [Docker Bake is Now Generally Available in Docker Desktop 4.38!](https://www.docker.com/blog/ga-launch-docker-bake/)
[^2]: [Introduction to Bake](https://docs.docker.com/build/bake/introduction/)
