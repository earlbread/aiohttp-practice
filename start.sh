#!/bin/bash

set -euo pipefail

service nginx start
pipenv run python -m aiohttp_practice --port=8081
