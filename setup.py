#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tgnotify',
    version='1.0',
    packages=find_packages()+['src'],
    scripts=[
    'src/TelegramNotify.py'
    ]
)
