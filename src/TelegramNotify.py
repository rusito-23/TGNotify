#!/usr/bin/env python

import argparse
from . import TelegramBotAPI as TG
from .Constants import BOLD, ITALIC

def send_message(title, subtitle):
    # create message
    title = BOLD.format(title)
    subtitle = ITALIC.format(subtitle)
    TG.send_message(title, subtitle)

def main():
    # arguments
    description = 'Simply send a Telegram message.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--title', required=True, dest='title')
    parser.add_argument('--subtitle', required=True, dest='subtitle')
    args = parser.parse_args()
    # send
    send_message(args.title, args.subtitle)

if __name__ == '__main__':
    main()
