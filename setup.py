#!/usr/bin/env python

from setuptools import setup, find_packages

description = """
Telegram notification scripts!
- tgnotify
- tgcommandnotify
- tgnetnotify
"""
setup(
    name='TGNotify',
    version='1.0',
    description=description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tgnotify = src.TelegramNotify:main',
            'tgcommandnotify = src.TelegramCommandNotify:main',
            'tgnetnotify = src.TelegramNetworkNotify:main'
        ]
    }
)
