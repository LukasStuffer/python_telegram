#!/usr/bin/env python3

# Lukas Stuffer
# IG: _lukasstuffer_

import requests
import json

class TelegramNotification:

    def __init__(self, token: str, chat_id=[], txt='Telegram sent successfully.'):

        self.token      = token
        self.chat_id    = chat_id
        self.txt        = txt


    def send(self):

        try:
            
            for cid in self.chat_id:

                url = 'https://api.telegram.org/bot' + self.token + '/sendMessage'
                payload = {'chat_id': cid, 'text': self.txt}

                r = requests.post(url, data=payload)

            print("Telegram send successfully")

        except:

            print("Telegram send failed!")
