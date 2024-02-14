Send a message via Telegram with python3

Installation:
Copy notification_telegram.py into your project folder

Example (main.py):
```python
#!/usr/bin/python3

# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
# https://core.telegram.org/bots/api

from notification_telegram import TelegramNotification

if __name__ == "__main__":
  
  telegram = TelegramNotification(token='2834145567:FASRQWXDakJCEd2T7q1kLU2Zm3j4fDSaJ0A')
  
  telegram.chat_id    = ['1356462978']
  telegram.txt        = 'Telegram sent successfully.'
  telegram.send()
