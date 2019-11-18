#! /usr/bin/python3

# HELP FUNCTIONS

def print_help_env_vars():
    print("ERROR: Please set your TELEGRAM BOT ACCOUNT environment variables: ")
    print("TG_TOKEN")
    print("TG_CHAT_ID")

# MAIN FUNCTIONS

def send_msg(body):
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
