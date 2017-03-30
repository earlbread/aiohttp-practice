# [aiohttp][] practice

## 1. Setup environment

aiohttp requires Python 3.5 or newer. Also you need to install [pipenv][].

```bash
$ pip install pipenv
```

If you are using pyenv, you need to set environment variable below:

```bash
$ export PIPENV_SHELL_COMPAT=1
```

or

```bash
$ export PIPENV_VENV_IN_PROJECT=1
```

After install Python 3.5 and pipenv, you can install dependencies.

```bash
$ git clone https://github.com/earlbread/aiohttp-practice.git
$ cd aiohttp-practice
$ pipenv install
```

[aiohttp]: https://github.com/aio-libs/aiohttp
[pipenv]: https://github.com/kennethreitz/pipenv
