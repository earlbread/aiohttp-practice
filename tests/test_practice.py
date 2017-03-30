from aiohttp import web

from aiohttp_practice.views import index

async def test_hello(test_client, loop):
    app = web.Application()
    app.router.add_get('/', index)
    client = await test_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello world' in text
