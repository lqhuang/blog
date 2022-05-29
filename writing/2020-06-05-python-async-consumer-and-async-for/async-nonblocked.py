import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    tic = time.time()

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Nothing happens if we just call
    #     task1 = say_after(1, 'hello')
    #     task2 = say_after(2, 'hello')
    # two coroutine objects are created but not awaited,
    # so it *won't run at all*.
    # Of course, another option in this situation is to use
    #     await asyncio.gather(*(task1, task2))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(
        f"finished at {time.strftime('%X')}, elapsed time: {time.time() - tic}s"
    )


asyncio.run(main())
