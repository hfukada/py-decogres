#!/usr/bin/env python

from setuptools import setup
__version__ = '1.0.4'

with open('requirements.txt') as f:
        required = f.read().splitlines()
setup(
    name='decogres',
    version=__version__,
    description='Postgresql decorator',
    author='Hiroshi Fukada',
    author_email='hiroshi@fukada.us',
    packages=['decogres'],
    url='https://github.com/hfukada/py-decogres',
    download_url='https://github.com/hfukada/py-decogres/tarball/%s' % __version__,
    install_requires=required
)
