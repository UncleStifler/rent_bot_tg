
from ui.utils import search_bd

def filter_to_ui(filter, db):
    filter = filter[0]
    type_ = 'flats' if filter['type'] == 0 else 'rooms'
    city = '*Barcelona*'
    district = search_bd(filter['district'], db.districts)
    address = ' in '
    if district:
        address += f'*{district}*, {city}'
    else:
        address += city
    text = f'Filter - *{filter["name"]}*\nSearching *{type_}*{address}'

    if filter['rooms']:
        rooms = f'*{filter["rooms"]} rooms*'
    else:
        rooms = None

    if filter['min_price'] and filter['max_price']:
        price = f'between *{filter["min_price"]}* and *{filter["max_price"]}*'
    elif filter['min_price']:
        price = f'above *{filter["min_price"]}*'
    elif filter['max_price']:
        price = f'under *{filter["max_price"]}*'
    else:
        price = None

    if rooms and price:
        rooms_price = f'{rooms} with a price {price} euros'
    elif rooms:
        rooms_price = rooms
    elif price:
        rooms_price = f'With a price {price} euros'
    else:
        rooms_price = None

    if rooms_price:
        text += f'\n{rooms_price}'

    sex = None
    if filter['sex']:
        if filter['sex'] == 0:
            sex = 'both gender'
        elif filter['sex'] == 1:
            sex = 'only male'
        elif filter['sex'] == 2:
            sex = 'only female'
    pets = None
    if filter['pets']:
        pets = True
    smoke = None
    if filter['smoke']:
        smoke = True
    owner = None
    if filter['owner']:
        owner = True

    t = f'\nYou a searching property'
    if sex:
        t += f' for a *{sex}*'
    if pets and smoke:
        t += ' with a *pets* and *smoke* allowed'
    elif pets:
        t += ' with a *pets* allowed'
    elif smoke:
        t += ' with a *smoke* allowed'
    if owner:
        t += ' where landlord is the *owner* of property'

    if sex or pets or smoke or owner:
        text += t

    #todo routes
    return text