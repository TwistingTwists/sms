#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
from setuptools import setup
# from disutils.core import setup

NAME = 'sms'
VERSION = '1.0'

if __name__ == "__main__":
    setup(
            name = NAME,
            version = VERSION,
            author = 'Abhishek Tripathi',
            author_email = 'abhishek.tripathi456@gmail.com',
            description = 'Personal smsing module',
            url = 'https://github.com/TwistingTwists/sms'
            packages = ['sms'],
            entry_points = {
                'console_scripts': [
                    'sms = sms.send:main'
                    ]
                },
            )
