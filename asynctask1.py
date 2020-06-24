import asyncio


@asyncio.coroutine
def hello(name):
    for i in range(10):
        print("hello %s %d" % (name, i))
        yield


async def main(loop):
    tasks = [loop.create_task(hello(name)) for name in("A", "B", "C")]

    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
