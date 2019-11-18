import os
import sys
import subprocess
import requests
from subprocess import PIPE

# HELP FUNCTIONS

def print_help_env_vars():
    print("ERROR: Please set your TELEGRAM BOT ACCOUNT environment variables: ")
    print("TG_TOKEN")
    print("TG_CHAT_ID")

# MAIN FUNCTIONS

def notify(hostname):
    try:
        # Set account vars
        tgToken = os.environ['TG_TOKEN']
        chatID = os.environ['TG_CHAT_ID']
    except KeyError:
        print_help_env_vars()

    # Create message body
    body = "Internet is back up pedazo de vago!"
    "Go back to work! Ping to: {} was succesfull!".format(hostname)
    print(body)

    # Send msg
    PARAMS = { 'chat_id' : chatID, \
               'text' : body }
    URL = 'https://api.telegram.org/bot{}/sendMessage'.format(tgToken)
    r = requests.get(url = URL, params = PARAMS)
    print("STATUS_CODE: {}".format(r.status_code))

def main():

    # Ping until connection reached
    hostname = sys.argv[1]
    ping_cmd = "ping -c 1 {} ".format(hostname)
    res = 1
    while res != 0:
        process = subprocess.Popen(ping_cmd,
                                    stdout=PIPE,
                                    stderr=PIPE,
                                    shell=True)
        process.wait()
        res = process.returncode

    print("Ping succesfull!")
    notify(hostname)


if __name__ == '__main__':
    main()
