import time
import asyncio


async def g():
    for i in range(5):
        print(f"Producer: create event A{i} -> {i}")
        await asyncio.sleep(i)
        yield i


async def producer(queue):
    async for i in g():
        await queue.put(i)
    await queue.put(None)

async def consumer(queue):

    # x = await queue.get()
    while ((x := await queue.get()) is not None):
        d = 2 * x
        print(f"Consumer: process event B{x} -> {x} * 2 = {d}")
        await asyncio.sleep(d)

async def main():
    tic = time.time()
    queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue),
        return_exceptions=False,
    )
    await queue.join()

    print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
