import requests

webhook = {'url': 'https://6772be23b77b.ngrok.io/rent_bot/'}

def get_url():
    url = "https://api.telegram.org/bot1684036818:AAEi2WyLSxlRTZoAexdH5zEeG9JeoeI3lKQ/setWebhook"
    r = requests.post(url, data=webhook)

#get_url()

def get_info():
    url = "https://api.telegram.org/bot1684036818:AAEi2WyLSxlRTZoAexdH5zEeG9JeoeI3lKQ/getWebhookInfo"
    r = requests.post(url)
    print(r.json())

#get_info()






#kde092

#1490631920:AAHCSpYQ_DjzqnbgpmcJiM2eZIBMLi-wSDk