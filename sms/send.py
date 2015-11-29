from twilio.rest import TwilioRestClient
from twilio.rest.resources import Connection
from twilio.rest.resources.connection  import PROXY_TYPE_HTTP
import sys

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "xxx"
auth_token  = "xxx"

#-----------------------------------------------------------------------------------------
# Proxy settings, like you want, use PROXY_TYPE_SOCKS5 for socks proxy
Connection.set_proxy_info(
    '10.3.100.207',  #proxy server
    8080,               #port
    proxy_type=PROXY_TYPE_HTTP,
    )
#-----------------------------------------------------------------------------------------

client = TwilioRestClient(account_sid, auth_token)

def print_error():
    print("Usages : sms [name] ['message']")

def send_message(num,text="Sample Text"):
    message = client.messages.create(body=text,
        to=num,                                     # Replace with your phone number
        from_="+1234567889")               # Replace with your Twilio number
    print ("[{}] -> {} ".format(message.sid,message.body))

def who(s):
    if s == 'person1_name':
        num  = "+911234567890" # 10 digit mobile number of that person
    elif s == 'person2_name':
        num = "+911234567890"
    elif s == 'me':
        num = "+911234567890" # your phone number
    return num

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
    num = who(command[0])

    ## in case I cannot find whose number, revert the message to you ;)
    if not num:
        print ("message reverted to you.")
        num = "+911234567890"           #your number
    text = command[1]

    print ("{} to {}.".format(text,num))
    send_message(num,text)

