import asyncio
import time
import random
@asyncio.coroutine
def hello(name):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        print("hello, %s %d" % (name, i))
        yield


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(hello("A"), hello("B"), hello("C")))
