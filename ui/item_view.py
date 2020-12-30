
import ujson

from ui.utils import search_bd

def item_to_ui(db, item, fresh=False):
    if fresh:
        fresh = 'Found a new ad for you'
    else:
        fresh = 'This is an old ad'

    if item['sex'] == 0:
        sex = '*Both* gender'
    elif item['sex'] == 1:
        sex = '*Male* only'
    elif item['sex'] == 2:
        sex = '*Female* only'
    else:
        sex = '*Couple allowed*'
    if item['pets']:
        pets = '*Pets* allowed'
    else:
        pets = '*No pets* allowed'
    if item['smoke']:
        smoke = '*Smoke* allowed'
    else:
        smoke = '*No smoke* allowed'
    demands = f'{sex}\n{pets}\n{smoke}\n' if item['type'] == 1 else ''
    if item['owner']:
        owner = 'Landlord is the *owner*'
    else:
        owner = 'Landlord is *not* the *owner*'

    try:
        data = ujson.loads(item['amenities'])['amenities']
        amenities = f"Amenities: {', '.join([f'*{x}*' for x in data])}".replace('/', '\\')
    except KeyError:
        amenities = ''

    if item['contact_name'] and item['contact_phone']:
        contact_name = item['contact_name'].replace('\\t', '')
        contacts = f"\nContacts: *{contact_name}* - *{item['contact_phone']}*".replace('/', '\\')
    else:
        contacts = ''

    title = item['title'].replace('/', '\\')
    description = item['description'].replace('\\n', '\n').replace('/m', '').replace('/', '\\')

    type = 'Flat' if item['type'] == 0 else 'Room'
    city = search_bd(item['city'], db.cities)
    district = search_bd(item['district'], db.districts)
    if item['url']:
        url = f'\n[Link]({item["url"]})'
    else:
        url = ''
    if item['photo']:
        # text += f'\n<a href="{item["photo"]}">&#8205;</a>'
        photo = f'[\u200B]({item["photo"]})'
    else:
        photo = ''
    text = f'''
{photo}{fresh} by filter "*{item['name']}*"
*{district}*, *{city}*
*{type}*, *{item['price']} €\month*, *{item['rooms']} rooms*
{demands}{owner}{contacts}
{amenities}{url}

*{title}*
_{description}_
'''
    text = text.replace('`', "'")
    return text