# twitter-status-bot
A simple Twitter status bot for my Raspberry Pi

## Required Packages:
- python-twitter: https://github.com/bear/python-twitter
- gpiozero: https://github.com/gpiozero/gpiozero

## Usage:
1. Get an Twitter-Account and register as a developer
2. modify config/twitter_api_keys.py and add your consumer key, consumer secret, api key and api secret.
3. modify confi/config.py to change the frequency of how often a tweet should be sent
4. you can modify the stauts message by editing the __getStatusMessage__(): function in jobs.py
