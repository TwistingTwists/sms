## sms

A simple SMSing [twilio](https://www.twilio.com/) wrapper. Only a few steps away from sending yourself message-alerts. 

## Installation:
```
git clone https://github.com/TwistingTwists/sms.git
cd sms
python setup.py install
```
## configuration:
Well, to use this, there a few things you need to configure correctly.

* account_sid  and auth_token from https://www.twilio.com/user/account/settings 
* proxy, if any 
    - if you are not using proxy, please delete the following portion from `sms/send.py` file.
        ```
        Connection.set_proxy_info(
            '10.3.100.207',  #proxy server
            8080,               #port
            proxy_type=PROXY_TYPE_HTTP,
            )

        ```
* add numbers to 'verified numbers' at https://www.twilio.com/user/account/phone-numbers/verified

##Usage:
`sms me "Yeay Let's eat!"`
Caution : Please use double quotes. 

###Exciting usages : 
 * Parse a webpage for updates. Notify yourself on update.
 * Ideas? All other wonderful implementations are welcome at [issues](https://github.com/TwistingTwists/sms/issues) page.
 * 
