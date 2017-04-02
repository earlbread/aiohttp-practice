import argparse
import asyncio
import sys

from aiohttp import web

from aiohttp_practice.routes import setup_routes

def main(args):
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    setup_routes(app)
    web.run_app(app, port=int(args.port))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port')

    args = parser.parse_args()

    main(args)
