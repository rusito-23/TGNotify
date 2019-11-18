import os
import sys
import subprocess
import requests

# HELP FUNCTIONS

def print_help_env_vars():
    print("ERROR: Please set your TELEGRAM BOT ACCOUNT environment variables: ")
    print("TG_TOKEN")
    print("TG_CHAT_ID")

# MAIN FUNCTIONS

def send_msg(command, output):
    try:
        # Set account vars
        tgToken = os.environ['TG_TOKEN']
        chatID = os.environ['TG_CHAT_ID']
    except KeyError:
        print_help_env_vars()
        return

    # Create message body
    message = "-------- RESPONSE -------- \n" + \
              "Command " + command + " finished running! \n" + \
              "Go back to work you lazy piece of crap! \n\n"
    body =  message + \
           "--------  OUTPUT  -------- \n" + \
           output

    print(message)

    # Send msg
    PARAMS = { 'chat_id' : chatID, \
               'text' : body }
    URL = 'https://api.telegram.org/bot{}/sendMessage'.format(tgToken)
    r = requests.get(url = URL, params = PARAMS)
    print("STATUS_CODE: {}".format(r.status_code))

def main():

    # Run given command
    command = " ".join(sys.argv[1:])
    zsh_command = "/bin/zsh -i -c '{}'".format(command)
    print(zsh_command)
    process = subprocess.Popen(zsh_command,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    out, err = process.communicate()

    if (process.returncode == 0):

        out = out.decode("utf-8")
        print(out) # print stdout

        send_msg(command, out)
    else:

        err = err.decode("utf-8")

        send_msg(command, err)
        print("-------- RESPONSE {} -------- \n\n {}" # print stderr
                    .format(process.returncode, err))


if __name__ == '__main__':
    main()
