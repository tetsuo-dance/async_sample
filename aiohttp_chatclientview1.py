import asyncio
import aiohttp


async def run():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            while True:
                try:
                    async for msg in ws:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            print(msg.data)
                            break
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            print("somethin wrong with message")
                            break
                except KeyboardInterrupt:
                    print("end of chat")
                    break
            await ws.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
