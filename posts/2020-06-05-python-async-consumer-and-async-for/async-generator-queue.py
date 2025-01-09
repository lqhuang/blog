import time
import itertools
import asyncio


async def producer(total):
    for i in range(total):
        print(f"Producer: create event A0 -> {i}")
        await asyncio.sleep(i)
        yield i


async def consumer(source):
    async for i in source:
        d = 2 * i
        print(f"Consumer: process event {i} -> {d}")
        await asyncio.sleep(2 * i)
        yield d


async def main():
    tic = time.time()
    async for i in consumer(producer(5)):
        print(f"Output  : output event B{i} -> {i}")
        print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
