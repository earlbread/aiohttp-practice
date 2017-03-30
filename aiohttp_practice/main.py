import argparse
import asyncio
import sys

from trafaret_config import commandline

from aiohttp import web

from aiohttp_practice.routes import setup_routes
from aiohttp_practice.utils import TRAFARET


def main(argv):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(ap,
                                          default_config='./config/practice.yaml')
    options = ap.parse_args(argv)
    config = commandline.config_from_options(options, TRAFARET)
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app['config'] = config
    setup_routes(app)
    web.run_app(app,
                host=app['config']['host'],
                port=app['config']['port'])

if __name__ == '__main__':
    main(sys.argv[1:])
