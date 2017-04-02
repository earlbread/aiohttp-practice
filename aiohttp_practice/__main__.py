import sys
import argparse
from aiohttp_practice.main import main

parser = argparse.ArgumentParser()
parser.add_argument('--port')

args = parser.parse_args()

main(args)
