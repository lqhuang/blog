---
title: Unifying the CUDA C++ Core Libraries
date: 2023-10-07
tags:
  - dev
---

> We're excited to announce that the CUDA C++ Core Libraries (CCCL) - Thrust,
> CUB, and libcudacxx - are now unified under the nvidia/cccl repository.
>
> -- Jake Hemstad (@jrhemstad) on GitHub[^unifying]

- [thrust](https://github.com/NVIDIA/thrust): The C++ parallel algorithms
  library.
- [cub](https://github.com/NVIDIA/cub): Cooperative primitives for CUDA C++.
- [libcudacxx](https://github.com/NVIDIA/libcudacxx): The C++ Standard Library
  for your entire system.

I delightful love news / work like unifying abstractions. It makes me peace,
relaxy and makes everything robuster.

Refs:

- [NVIDIA/cccl](https://github.com/NVIDIA/cccl): CUDA C++ Core Libraries
- [Bundle CCCL in CuPy #7851](https://github.com/cupy/cupy/pull/7851)

[^unifying]: [Unifying the CUDA C++ Core Libraries: Towards a More Delightful CUDA C++ #520](https://github.com/NVIDIA/cccl/discussions/520)
