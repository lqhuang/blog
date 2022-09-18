---
title: 并查集
created: 2019-09-04 14:53
draft: True
---

## 愚蠢版

```python
a = []
b = []
for elem in reversed(a):
    if elem in b:
        a.remove(elem)
```

显然...这个方法是 0(n2) 的.

使用 set

```python
a = set(a)
b = set(b)

diff = a - b
# or
diff = a.difference(b)

# if a is an another iterable object
for elem in diff：
    a.remove(elem)
# else if a is a set, that's much more simple
a.dlfference_update(b)
```

So here is the question

how does python's set difference work internally?

https://stackoverflow.com/questtons/15524753/how-does-python-set-difference-work-tnternally

Python sets are open-addressing hashtables with a prime probe. In other words every set value can be looked up quickly because it was inserted in such a way (hashed) to differentiate it and find it (not order it) from other values.

https://github.com/python/cpython/blob/675d17cec49ed7f7eb01d1bc3ae6999c728e070d/Objects/setobject.c#L1540
https://github.com/python/cpython/blob/master/Objects/setobject.c#L1540

## Symmetric difference of two sorted array

https://www.geeksforgeeks.org/symmetric-difference-two-sorted-array/

## References

https://arxiv.org/abs/1301.3388
https://cs.stackexchange.com/questions/17984/computing-set-difference-between-two-large-sets
https://en.wikipedia.org/wiki/Bit_array
https://en.wikipedia.org/wiki/Embarrassingly_parallel

O(NlogN) -> https://en.cppreference.com/w/cpp/algorithm/set_difference

If you're using C++, there is support in the standard library for this (std::set_difference)
http://www.cplusplus.com/reference/algorithm/set_difference/
That documentation even includes equivalent "pseudocode" (really, just more C++) that you can use to port the idea to other languages. The algorithm is close to the "merging" part of mergesort. Note that std::set_difference operates upon sorted ranges, not std::sets (this is a good thing - means sorted std::vector's are adequate).

## bitmap

https://mp.weixin.qq.com/s?__biz=MzI3MDU3OTc1Nw==&mid=2247485964&idx=1&sn=01150b8d051c661013aede2a403216dc&chksm=eacfab4eddb822587d1a645764a0b4773406ded1f7324e44b105adc17e44fd19b1fa3fac7b4b&mpshare=1&scene=1&srcid=1020HqlpVfkyeH0E5mS3Tnec&sharer_sharetime=1634706901957&sharer_shareid=a02c97b66753e49e61e3def16e4d4411&exportkey=Aa8jdY%2BGW4yVlxBh%2Boi8ews%3D&pass_ticket=wtr8TXsmoU4lDteb%2B3vcOhQ0CZSDaSf73sBqgaYYQ3y4qG1u7akV9GAmKQVFsuH8&wx_header=0#rd
