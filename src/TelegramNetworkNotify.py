#!/usr/bin/env python

import sys
import subprocess
from subprocess import PIPE
from contextlib import suppress

from . import TelegramBotAPI as TG
from .Constants import BOLD, ITALIC
from .Constants import DEFAULT_HOST

def notify():
    title = BOLD.format('Internet is back up!')
    subtitle = ITALIC.format('Now sit & get back to work . . .')
    TG.send_message(title, '', subtitle)

def ping():
    # ping until connection reached
    hostname = DEFAULT_HOST
    with suppress(IndexError): hostname = sys.argv[1]
    ping_cmd = 'ping -c 1 {} '.format(hostname)
    res = 1
    while res != 0:
        process = subprocess.Popen(ping_cmd,
                                    stdout=PIPE,
                                    stderr=PIPE,
                                    shell=True)
        process.wait()
        res = process.returncode

    notify()

def main():
    ping()

if __name__ == '__main__':
    main()
