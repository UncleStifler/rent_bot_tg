
import ui.lang_lines as ll
import ui.lang_buttons as lb
from ui.utils import search_bd
from backend.photos import get_photo_url
from ui.utils import normalize_text
from backend.filter_adding.view import (sex_view,
                                        pets_view,
                                        smoke_view,
                                        owner_view)

def get_ad_text(ad, db, lang='en'):
    id_ = ad['id']
    photo_url = get_photo_url(ad['photo'].split('/')[1])
    photo = f'[\u200B]({photo_url})'
    # todo title descr
    print(photo)
    print(ad)
    text = f'''
{photo}
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