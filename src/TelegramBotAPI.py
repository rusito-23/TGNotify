#! /usr/bin/python3
import requests
import os

# PATHS

BASE_URL='https://api.telegram.org/bot{}'
SEND_MESSAGE_URL=BASE_URL+'/sendMessage'
GET_UPDATES_URL=BASE_URL+'/getUpdates'

# STYLES

BOLD="<b>{}</b>"
ITALIC="<i>{}</i>"

# COLORS
GREEN = '\033[92m'
RED="\033[31m"
BLUE="\033[34m"
MAGENTA="\033[35m"
WARNING = '\033[93m'
BLANK="\033[0m"

# HELPERS

def get_environment_vars():
    try:
        token = os.environ['TG_TOKEN']
        chat_id = os.environ['TG_CHAT_ID']
        return (token, chat_id)
    except KeyError:
        print(f"""
{RED}------- ERROR -------{BLANK}
Set your {MAGENTA}TELEGRAM BOT ACCOUNT{BLANK} \
environment variables:
{BLUE}- TG_TOKEN
{BLUE}- TG_CHAT_ID{BLANK}
        """)
        exit(1)

def get(url, params):
    req = requests.get(url=url, params=params)
    if req.status_code in range(200, 300):
        print(f"""
{GREEN}-------- NICE ------ {BLANK}
Your notification was sent successfully!
        """)
    else:
        print(f"""
{RED}------- ERROR -------{BLANK}
The request failed with Request Code: {WARNING}{req.status_code}{BLANK}
Maybe the TG_CHAT_ID has expired!
        """)
        exit(1)

# METHODS

def send_message(title, body, subtitle=None):
    token, chat_id = get_environment_vars()

    # build message
    message = BOLD.format(title) + "\n"
    if subtitle: message += ITALIC.format(subtitle) + "\n"
    message += body
    print(message)

    # send
    params = {'chat_id' : chat_id, 'text' : message, 'parse_mode' : 'html'}
    url = SEND_MESSAGE_URL.format(token)
    get(url, params)
