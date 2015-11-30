from twilio.rest import TwilioRestClient
from twilio.rest.resources import Connection
import json
from data import module_locator

json_path = module_locator.modeule_path()

# with open("./"+json_path+"/"+'config.json','r') as f:
with open(json_path+"/"+'config.json','r') as f:
    conf = json.load(f)

from twilio.rest.resources.connection  import PROXY_TYPE_SOCKS5, PROXY_TYPE_HTTP
import sys



# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = conf['auth']['AuthSid']
auth_token  = conf['auth']['AuthToken']

#-----------------------------------------------------------------------------------------
# Proxy settings, like you want, use PROXY_TYPE_SOCKS5 for socks proxy
if (conf['proxy']['ProxyType'] == "HTTP"):
    Connection.set_proxy_info(
        str(conf['proxy']['Proxy']),
        conf['proxy']['Port'],
        proxy_type=PROXY_TYPE_HTTP,
        )

else:
    Connection.set_proxy_info(
        str(conf['proxy']['Proxy']),  #proxy server
        conf['proxy']['Port'],               #port
        proxy_type=PROXY_TYPE_SOCKS5)
#-----------------------------------------------------------------------------------------

client = TwilioRestClient(account_sid, auth_token)

def print_error():
    print("Usage : sms [name] ['message']")
    print("Define `name` in `config.json`. ")

def send_message(num,text=conf['user']['default_message']):
    message = client.messages.create(body=text,
        to=num,
        from_= conf['personal']['your_twilio_number']    )
    print ("[{}] -> {} to {}".format(message.sid,message.body,num))



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
    s = command[0]
    num = []
    text = []

    num = conf['personal']['verified_numbers'][s]

    ## in case I cannot find whose number, revert the message to you ;)
    if not num:
        print ("message reverted to you.")
        num = conf['personal']['your_twilio_number']          #your number
    text = command[1]

#    print ("{} to {}.".format(text,num))
    send_message(num,text)

