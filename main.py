import asyncio
from aiohttp import web

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
web.run_app(app, host='127.0.0.1', port=8080)
