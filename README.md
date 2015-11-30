## sms

A simple SMSing [twilio](https://www.twilio.com/) wrapper. Only a few steps away from sending yourself message-alerts. 

### Steps to use `sms`:

1. Sign Up at [twilio](http://twilio.com/).
2. Get your first twilio number
3. Verifiy phone numbers 
4. Find `auth_sid` and `auth_token` on settings page.


### User Configuration:
Configuration file = `/data/config.json`
 
 **Note**: (for following in `/data/config.json`)

 *   `Custome_name_one` in `verified_numbers` is a custom name. It can be anything as user likes.
 *   `default_message`


### Installation:
```
git clone https://github.com/TwistingTwists/sms.git sms
cd sms
python setup.py install
```

###Usage:
`sms me "Yeay Let's eat!"`
Caution : Please use double quotes. `me` is a `Custom_name` defined by user.
>*incorrect usage* :
> sms me Yeay Let's eat! 

### FAQs:

* #####Can I use to send messages to any phone number?
> yes. If only you have a paid twilio account. Free service includes sending messages to ONLY your verfied numbers.

* ##### Have confusion/questions? Please use   [issues](https://github.com/TwistingTwists/sms/issues) page.

###Exciting usages : 
 * Parse a webpage for updates. Notify yourself on update.
 * Ideas? All other wonderful implementations are welcome at [issues](https://github.com/TwistingTwists/sms/issues) page.
 * 
