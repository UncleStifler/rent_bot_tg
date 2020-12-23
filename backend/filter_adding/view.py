
from ui.utils import search_bd

def type_view(type):
    if type is None:
        return 'Both'
    elif type == 0:
        return 'Flat'
    elif type == 1:
        return 'Room'

def city_view(city, db):
    if not city:
        return 'None'
    else:
        return search_bd(city, db.cities)

def district_view(district, db):
    if district['city'] is None:
        return 'Select city to select district'
    if not district['district']:
        return 'None'
    else:
        return search_bd(district['district'], db.districts)

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
    elif sex == 3:
        return 'Couple'
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
City - *{city_view(filter['f_filter']['city'],
                   db)}*
District - *{district_view(filter['f_filter'],
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
