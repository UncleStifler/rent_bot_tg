import requests
from config import TOKEN
from time import sleep


def posting(user_id, text):
    url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'
    r = requests.post(url, data={'chat_id': user_id, 'text': text})
    sleep(0.1)
    # print(r.json())
    if r.status_code == 200:
        return True
    else:
        return False
