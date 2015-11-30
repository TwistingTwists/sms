from twilio.rest import TwilioRestClient
from twilio.rest.resources import Connection
import json

with open('../config.json','r') as f:
    confif = json.load(f)

from twilio.rest.resources.connection  import conf['proxy']['ProxyType']
import sys



# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = config['auth']['AuthSid']
auth_token  = config['auth']['AuthToken']

#-----------------------------------------------------------------------------------------
# Proxy settings, like you want, use PROXY_TYPE_SOCKS5 for socks proxy
if conf['proxy']['use_proxy']:
    Connection.set_proxy_info(
        conf['proxy']['Proxy'],  #proxy server
        conf['proxy']['Port'],               #port
        proxy_type=conf['proxy']['ProxyType']
        )
#-----------------------------------------------------------------------------------------

client = TwilioRestClient(account_sid, auth_token)

def print_error():
    print("Usage : sms [name] ['message']")
    print("Define `name` in `config.json`. ")

def send_message(num,text=conf['user']['message']):
    message = client.messages.create(body=text,
        to=num,                                     # Replace with your phone number
        from_= conf['personal']['your_twilio_number']             # Replace with your Twilio number
    print ("[{}] -> {} ".format(message.sid,message.body))

def  main_oldy():
    """
    This is the old implementation.
    usage : sms -n me -t "forget to eat!"
    """
    command = sys.argv[1:]
    if not command:
        print_error()
        sys.exit(2)

    if command[0] == '-n':
        num = who(command[1])
    if command[2] == '-t':
        text = command[3]
    send_message(num,text)



def  main():
    """
    usage : sms me "forget to eat!"
    ErrorCase: sms me forget to eat!
    the message is only 'forget', rest of the string is ignored. So, please use double quotes
    """
    command = sys.argv[1:]
    if not command:
        print_error()
        sys.exit(2)
    print (command[0])
    num = []
    text = []
    # num = who(command[0])
    num = conf['personal']['verified_numbers'][s]

    ## in case I cannot find whose number, revert the message to you ;)
    if not num:
        print ("message reverted to you.")
        num = conf['personal']['your_twilio_number']          #your number
    text = command[1]

    print ("{} to {}.".format(text,num))
    send_message(num,text)

