from setuptools import setup

setup(
    name='aiohttp_practice',
    packages=['aiohttp_practice'],
    include_package_data=True,
    install_requires=[
        'aiohttp',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
