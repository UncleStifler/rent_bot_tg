
import ujson


import ui.lang_lines as ll
import ui.lang_buttons as lb
from ui.utils import search_bd
from backend.photos import get_photo_url

def item_to_ui(db, item, lang, fresh=False):
    if fresh:
        fresh = ll.fresh[lang]
    else:
        fresh = ll.not_fresh[lang]

    if item['sex'] == 0:
        sex = ll.both_gender[lang]
    elif item['sex'] == 1:
        sex = ll.male_only[lang]
    elif item['sex'] == 2:
        sex = ll.female_only[lang]
    else:
        sex = ll.couple_allowed[lang]
    if item['pets']:
        pets = ll.pets_allowed[lang]
    else:
        pets = ll.no_pets_allowed[lang]
    if item['smoke']:
        smoke = ll.smoke_allowed[lang]
    else:
        smoke = ll.no_smoke_allowed
    demands = f'{sex}\n{pets}\n{smoke}\n' if item['type'] == 1 else ''
    if item['owner']:
        owner = ll.owner[lang]
    else:
        owner = ll.not_owner[lang]

    try:
        data = ujson.loads(item['amenities'])['amenities']
        amenities = f"{lb.amenities[lang]}: {', '.join([f'*{x}*' for x in data])}".replace('/', '\\')
    except KeyError:
        amenities = ''

    if item['contact_name'] and item['contact_phone']:
        contact_name = item['contact_name'].replace('\\t', '')
        contacts = f"\n{lb.contacts[lang]}: *{contact_name}* - *{item['contact_phone']}*".replace('/', '\\')
    else:
        contacts = ''

    title = item['title'].replace('/', '\\')
    description = item['description'].replace('\\n', '\n').replace('/m', '').replace('/', '\\')

    type = lb.flat[lang] if item['type'] == 0 else lb.room[lang]
    city = search_bd(item['city'], db.cities)
    district = search_bd(item['district'], db.districts)
    if item['url']:
        url = f'\n  [{lb.LINK}]({item["url"]})'
    else:
        url = ''
    if item['photo']:
        photo = item['photo']
        if photo.startswith('local/'):
            photo_id = photo.split('/')[1]
            photo = get_photo_url(photo_id)
        # text += f'\n<a href="{item["photo"]}">&#8205;</a>'
        photo = f'[\u200B]({item["photo"]})'
    else:
        photo = ''
    text = f'''
{photo}{fresh} by filter "*{item['name']}*"
*{district}*, *{city}*
*{type}*, *{item['price']} €\\{lb.month[lang]}*, *{item['rooms']} {lb.rooms[lang]}*
{demands}{owner}{contacts}
{amenities}{url}

    *{title}*
_{description}_
'''
    text = text.replace('`', "'")
    return text