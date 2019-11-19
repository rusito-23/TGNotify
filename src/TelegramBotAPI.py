#!/usr/bin/env python

import requests
import os
from Colors import *
from Constants import ASCII

# PATHS

BASE_URL='https://api.telegram.org/bot{}'
SEND_MESSAGE_URL=BASE_URL+'/sendMessage'
GET_UPDATES_URL=BASE_URL+'/getUpdates'

# HELPERS

def get_environment_vars():
    try:
        token = os.environ['TG_TOKEN']
        chat_id = os.environ['TG_CHAT_ID']
        return (token, chat_id)
    except KeyError:
        print(f'''
{RED}------- ERROR -------{BLANK}
Set your {MAGENTA}TELEGRAM BOT ACCOUNT{BLANK} \
environment variables:
{BLUE}- TG_TOKEN
{BLUE}- TG_CHAT_ID{BLANK}
        ''')
        exit(1)

def get(url, params):
    req = requests.get(url=url, params=params)
    if req.status_code in range(200, 300):
        print(f'''
{GREEN}-------- NICE -------- {BLANK}
Your notification was sent successfully!
        ''')
    else:
        print(f'''
{RED}------- ERROR -------{BLANK}
The request failed with Request Code: {WARNING}{req.status_code}{BLANK}
{WARNING}------- RESPONSE -------{BLANK}
{req.content.decode()}
        ''')
        exit(1)

# METHODS

def send_message(title, body, subtitle=None):
    token, chat_id = get_environment_vars()

    # build message
    message = title + '\n'
    if subtitle: message += subtitle + '\n'
    message += body

    # send
    params = {'chat_id' : chat_id,\
              'text' : message.encode(ASCII, 'replace'),\
              'parse_mode' : 'html'}
    url = SEND_MESSAGE_URL.format(token)
    get(url, params)
