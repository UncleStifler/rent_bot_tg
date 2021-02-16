
import ui.lang_lines as ll
import ui.lang_buttons as lb
from ui.utils import search_bd
from backend.photos import get_photo_url
from ui.utils import normalize_text
from backend.filter_adding.view import (sex_view,
                                        pets_view,
                                        smoke_view,
                                        owner_view)
#https://api.telegram.org/bot1684036818:AAEi2WyLSxlRTZoAexdH5zEeG9JeoeI3lKQ/sendphoto?chat_id=@testdjeziklog&photo="@api.telegram.org/file/bot1684036818:AAEi2WyLSxlRTZoAexdH5zEeG9JeoeI3lKQ/photos/file_11.jpg"
def get_ad_text(ad, db, lang='en'):
    id_ = ad['id']
    #if ad['photo']:
        #photo_url = ad['photo'].split('/')[1]#get_photo_url(int(ad['photo'].split('/')[1]))
        #print(photo_url)
        # должны получить file_id
        #photo_url = 'AgACAgIAAxkBAAIBCGAqbAF2vBVR1TudNM6VnT9i6-GxAALMsjEbDn9RSQo6E2_4EdH1WFQumy4AAwEAAwIAA3gAA-OiAgABHgQ'
        #photo = f'[\u200B]({photo_url})'
    #else:
        #photo = ''
    print(ad)
    text = f'''

Title: *{normalize_text(ad['title'])}*
Contact Name: *{normalize_text(ad['contact_name'])}*
Contact Phone: *{normalize_text(ad['contact_phone'])}*

City: *{search_bd(ad['city'], db.cities)}*
District: *{search_bd(ad['district'], db.districts)}*
Price: *{ad['price']} €*
Rooms: *{ad['rooms']}*

Gender: *{sex_view(ad['sex'], lang, direct=True)}*
Pets: *{pets_view(ad['pets'], lang, direct=True)}*
Smoke: *{smoke_view(ad['smoke'], lang, direct=True)}*
Owner: *{owner_view(ad['owner'], lang)}*

Description: *{normalize_text(ad['description'])}*
'''
    print(text)
    return id_, text