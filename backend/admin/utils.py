
import ui.lang_lines as ll
import ui.lang_buttons as lb
from ui.utils import search_bd
from backend.photos import get_photo_url

def get_ad_text(ad, db, lang):
    id_ = ad['id']
    photo = f"[\u200B]({get_photo_url(ad['photo'].split('/')[1])})"
    # todo title descr
    text = f'''{photo}
Title: *{ad['title']}*
Description: *{ad['title']}*
Contact Name: *{ad['contact_name']}*
Contact Phone: *{ad['contact_phone']}*

City: *{search_bd(ad['city'], db.cities)}*
District: *{search_bd(ad['district'], db.districts)}*
Price: *{ad['price']} €*
Rooms: *{ad['rooms']}*

'''
    return id_, text