import asyncio
import aiohttp


async def run():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            while True:
                try:
                    await ws.send_str(input(">>>"))
                except KeyboardInterrupt:
                    print("end of chat")
                    break
            await ws.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
