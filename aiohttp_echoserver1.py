from aiohttp import web
import logging
import aiohttp


async def websocket_handler(request):
    logger = logging.getLogger(__name__)
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        logger.info("collect data")
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print("error %s" % ws.exception())
        logger.info("closed")
        return ws

app = web.Application()
app.add_routes([web.get("/ws", websocket_handler)])

web.run_app(app, port=8080)
