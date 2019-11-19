#!/usr/bin/env python

import sys
import subprocess
import random
import TelegramBotAPI as TG
from Constants import BOLD, ITALIC
from Constants import UTF8

subtitles = ['Go back to work, you lazy piece of crap!',
            'Terminate rapidito el pucho y a seguir...',
            'No seas tan vagazo, que en cualquier momento te rajan']

def send_message(command, output):
    # clean output
    output = output.split(b'\x07')[-1].decode(UTF8)
    # create message
    title = f'Command {BOLD.format(command)} finished running!'
    subtitle = ITALIC.format(random.sample(subtitles, 1)[0])
    body = f'-------- {BOLD.format("OUTPUT")} -------- \n{output}'
    TG.send_message(title, body, subtitle)

def run_command():
    # run given command
    command = ' '.join(sys.argv[1:])
    zsh_command = "/bin/zsh -i -c '{}'".format(command)
    process = subprocess.Popen(zsh_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    # retrieve output
    out, err = process.communicate()
    output = out if not process.returncode else err

    # send output
    print(f'\n{output.decode(UTF8)}')
    send_message(command, output)

if __name__ == '__main__':
    run_command()
