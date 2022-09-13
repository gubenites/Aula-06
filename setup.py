#!/usr/bin/env python3
from setuptools import setup

setup_args = {
      "name" :'dev_aberto_gustavomfb',
      "version" : '0.1',
      "packages" : ['dev_aberto'],
      "author" : 'gustavomfb',
      "scripts" : ['scripts/hello.py'],
}

install_requires = [
      'requests'
]

setup(
      **setup_args, install_requires = install_requires
      )