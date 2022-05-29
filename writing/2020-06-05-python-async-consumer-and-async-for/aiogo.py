import asyncio
from functools import wraps


def gogenerator(aiterable=None, buffering=0):
    def decorator(aiterable):
        @wraps(aiterable)
        def wrapper(*args, **kwargs):
            return go(aiterable(*args, **kwargs), buffering)

        return wrapper

    if aiterable is None:
        return decorator
    return decorator(aiterable)


class go:
    def __init__(self, aiterable, buffering=0):
        self._task = None
        self._in_queue = None
        self._out_queue = None
        self._aiterator = None
        self._aiterable = aiterable
        self._buffering = buffering

    # Context management

    async def __aenter__(self):
        # Perform checks
        if self._task:
            raise RuntimeError("Goroutine already started")
        # Get maxsize
        if self._buffering < 0:
            maxsize = 0
        if self._buffering == 0:
            maxsize = 1
        else:
            maxsize = self._buffering
        # Initialize
        self._in_queue = asyncio.Queue(maxsize)
        self._out_queue = asyncio.Queue(maxsize)
        self._aiterator = self._aiterable.__aiter__()
        # Start the task
        self._task = asyncio.ensure_future(self._target())
        return self

    async def __aexit__(self, *args):
        # Close generator
        try:
            await self._aiterator.aclose()
        except AttributeError:
            pass
        # Clean up task
        self._task.cancel()
        try:
            await self._task
        except asyncio.CancelledError:
            pass
        # Reinitialize
        self._task = None
        self._in_queue = None
        self._out_queue = None
        self._aiterator = None

    # Synchronisation

    async def _target(self):
        coro = self._aiterator.__anext__()
        while True:
            # Get data from iterator
            try:
                value = await coro
            except Exception as exc:
                await self._out_queue.put((None, exc))
                return
            # Interrupt
            await self._out_queue.put((value, None))
            # Get data from user
            if self._buffering:
                value, exc = None, None
            else:
                value, exc = await self._in_queue.get()
            # Prepare next iteration
            if exc is not None:
                coro = self._aiterator.athrow(exc)
            elif value is not None:
                coro = self._aiterator.asend(value)
            else:
                coro = self._aiterator.__anext__()

    async def asend(self, value):
        # Enter if necessary
        if not self._task:
            await self.__aenter__()
        # Perform checks
        if value is not None:
            self._aiterator.asend
            assert not self.buffering
        # Send user data
        if not self._buffering:
            await self._in_queue.put((value, None))
        # Get iterator data
        value, exc = await self._out_queue.get()
        if exc is not None:
            raise exc
        return value

    async def athrow(self, exc):
        # Enter if necessary
        if not self._task:
            await self.__aenter__()
        # Perform checks
        self._aiterator.athrow
        assert not self._buffering
        # Send user exception
        await self._in_queue.put((None, exc))
        # Get user data
        value, exc = await self._out_queue.get()
        if exc is not None:
            raise exc
        return value

    # Asynchronous iteration

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await self.asend(None)


def test(step=.5):
    async def dots(n):
        for _ in range(n):
            await asyncio.sleep(step)
            print('.', end='', flush=True)
        print()

    async def agen():
        for x in range(3):
            yield await asyncio.sleep(step, x)

    @gogenerator
    async def even():
        async for x in agen():
            yield x * 2

    async def main():
        await dots(3)
        async for x in agen():
            print(x)

        print()

        async with go(agen()) as chan:
            await dots(3)
            async for x in chan:
                print(x)

        print()

        async with go(agen(), 1) as chan:
            await dots(3)
            async for x in chan:
                print(x)

        print()

        async with go(agen(), -1) as chan:
            await dots(3)
            async for x in chan:
                print(x)

        print()

        async with even() as chan:
            await dots(3)
            async for x in chan:
                print(x)

        print()

        async for x in even():
            print(x)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


if __name__ == '__main__':
    test()
