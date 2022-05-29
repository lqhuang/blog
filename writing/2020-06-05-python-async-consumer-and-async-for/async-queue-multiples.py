import time
import asyncio


async def g():
    for i in range(10):
        print(f"Producer: create event A{i} -> {i}")
        await asyncio.sleep(i * 0.1)
        yield i


async def producer(queue):
    async for i in g():
        await queue.put(i)


async def consumer(queue: asyncio.Queue):

    while True:
        x = await queue.get()
        d = 2 * x
        print(f"Consumer: process event B{x} -> {x} * 2 = {d}")
        await asyncio.sleep(d * 0.2)
        queue.task_done()  # to notify queue.join() task is completed


async def main():
    tic = time.time()
    queue = asyncio.Queue()

    producer_group = [asyncio.create_task(producer(queue)) for _ in range(4)]
    consumer_group = [asyncio.create_task(consumer(queue)) for _ in range(6)]

    await asyncio.gather(*producer_group, return_exceptions=False)

    print("Before join: done producing.")
    await queue.join()
    print("After join: If you don't use `task_done()` you wouldn't see this.")

    for t in consumer_group:
        t.cancel()

    print(f"elapsed time: {time.time() - tic}s")


if __name__ == '__main__':
    asyncio.run(main())
