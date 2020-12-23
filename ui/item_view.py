
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
    else:
        sex = '*Female* only'
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
        amenities = f"Amenities: {', '.join([f'*{x}*' for x in data])}"
    except KeyError:
        amenities = ''

    if item['contact_name'] and item['contact_phone']:
        contact_name = item['contact_name'].replace('\t', '')
        contacts = f"\nContacts: *{contact_name}* - *{item['contact_phone']}*"
    else:
        contacts = ''

    description = item['description'].replace('\\n', '\n')

    type = 'Flat' if item['type'] == 0 else 'Room'
    district = search_bd(item['district'], db.districts)
    text = f'''
{fresh} by filter "*{item['name']}*"
*{district}*, *Barcelona*
*{type}*, *{item['price']} €\month*, *{item['rooms']} rooms*
{demands}{owner}{contacts}
{amenities}

*{item['title']}*
{description}
'''

    if item['photo']:
        # text += f'\n<a href="{item["photo"]}">&#8205;</a>'
        text += f'\n[\u200B]({item["photo"]})'

    if '`' in text:
        text = text.replace('`', "'")
    return text