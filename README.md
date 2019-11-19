# TGNotify :love_letter:

Notification scripts for Telegram BOT

## Description

- **tgnotify**:

  This script is useful for commands with really long execution time.
  It takes a command as argument, executes it and then sends a Telegram message to notify the result.
  
 - **tgnetnotify** :coffee::
 
    Pings a host (default: *google.com*) until connection is reached, so you can drink a coffee while the internet is gone.

## Requirements

- **python 3.X**
- Libs listed in **requirements.txt** (pip install -r requirements.txt)
- Telegram BOT

  Setup the following Environment variables:
    - *TG_TOKEN*:  Telegram Bot token
    - *TG_CHAT_ID*:  Telegram Bot Chat ID with your user (http://api.telegram.org/botTOKEN/getUpdates)

## Install

Install dependencies and run: `python setup.py install`.
