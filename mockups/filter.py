
from ui.utils import search_bd

def type_view(type):
    if type is None:
        return 'None'
    elif type == 0:
        return 'Flat'
    elif type == 1:
        return 'Room'

def district_view(district, db):
    if not district:
        return 'None'
    else:
        return search_bd(district, db.districts)

def route_view(route, db):
    if not route:
        return 'None'
    else:
        return (search_bd(route, db.metro_routes) or (search_bd(route, db.bus_routes)))

def price_view(min_price, max_price):
    if min_price and max_price:
        return f'from *{min_price}* to *{max_price}* €'
    elif min_price:
        return f'more than *{min_price}* €'
    elif max_price:
        return f'less than *{max_price}* €'
    else:
        return 'None'

def rooms_view(filter):
    if filter['f_filter']['type'] == 1:
        return 'Only for flats'
    rooms = filter['f_filter']['rooms']
    if rooms:
        return str(rooms)
    else:
        return 'None'

def radius_view(radius):
    if radius:
        return f'{radius} km'
    else:
        return 'None'

def sex_view(filter):
    if filter['f_filter']['type'] == 0:
        return 'Only for rooms'
    sex = filter['f_filter']['sex']
    if sex == 0:
        return 'Both gender'
    elif sex == 1:
        return 'Male'
    elif sex == 2:
        return 'Female'
    else:
        return 'None'

def pets_view(filter):
    if filter['f_filter']['type'] == 0:
        return 'Only for rooms'
    pets = filter['f_filter']['pets']
    if pets:
        return 'Yes'
    else:
        return 'No'

def smoke_view(filter):
    if filter['f_filter']['type'] == 0:
        return 'Only for rooms'
    smoke = filter['f_filter']['smoke']
    if smoke:
        return 'Yes'
    else:
        return 'No'

def owner_view(owner):
    if owner:
        return 'Yes'
    else:
        return 'No'



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

def filter_from_memory(filter, db):
    return f'''
Filter - "*{filter['name']}*"
{f_type_from_memory(filter, main_view=True)}

*Price:*
{price_view(filter['f_filter']['min_price'],
             filter['f_filter']['max_price'])}

{f_loc_from_memory(filter, db, main_view=True)}

{f_other_from_memory(filter, main_view=True)}'''

def f_loc_from_memory(filter, db, main_view=False):
    up = '' if main_view else 'Current settings\n'
    return f'''{up}*Location:*
District - *{district_view(filter['f_filter']['district'],
                           db)}*
Public Transport - *{route_view(filter['g_filter']['route'],
                                db)}*
Distance to the stop - *{radius_view(filter['g_filter']['radius'])}*'''

def f_type_from_memory(filter, main_view=False):
    up = '' if main_view else 'Current settings\n'
    return f'''{up}*Property Type:*
Type - *{type_view(filter['f_filter']['type'])}*
Rooms - *{rooms_view(filter)}*'''

def f_other_from_memory(filter, main_view=False):
    up = '' if main_view else 'Current settings\n'
    return f'''{up}*Other:*
Gender - *{sex_view(filter)}*
Pets - *{pets_view(filter)}*
Smoke - *{smoke_view(filter)}*
Ownership - *{owner_view(filter['f_filter']['owner'])}*'''
