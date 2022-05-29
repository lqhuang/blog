import time
import asyncio


async def g():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    tic = time.time()
    async for x in g():
        print(x)
        await asyncio.sleep(2)
    print(f"elapsed time: {time.time() - tic}s")


if __name__ == "__main__":
    asyncio.run(main())
