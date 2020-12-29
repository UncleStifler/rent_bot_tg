
import ui.lang_buttons as lb
from ui.utils import search_bd

def type_view(type, lang):
    if type is None:
        return lb.both[lang]
    elif type == 0:
        return lb.flat[lang]
    elif type == 1:
        return lb.room[lang]

def city_view(city, db, lang):
    if not city:
        return lb.none_[lang]
    else:
        return search_bd(city, db.cities)

def district_view(district, db, lang):
    if district['city'] is None:
        return lb.district_constr[lang]
    if not district['district']:
        return lb.none_[lang]
    else:
        return search_bd(district['district'], db.districts)

def route_view(route, db, lang):
    if not route:
        return lb.none_[lang]
    else:
        return (search_bd(route, db.metro_routes) or search_bd(route, db.bus_routes) or search_bd(route, db.trains))

def price_view(min_price, max_price, lang):
    if min_price and max_price:
        return f'{lb.from_[lang]} *{min_price}* {lb.to_[lang].lower()} *{max_price}* €'
    elif min_price:
        return f'{lb.more[lang]} *{min_price}* €'
    elif max_price:
        return f'{lb.less[lang]} *{max_price}* €'
    else:
        return lb.none_[lang]

def rooms_view(filter, lang):
    if filter['f_filter']['type'] == 1:
        return lb.flats_constr[lang]
    rooms = filter['f_filter']['rooms']
    if rooms:
        return str(rooms)
    else:
        return lb.none_[lang]

def radius_view(radius, lang):
    if radius:
        return f'{radius} km'
    else:
        return lb.none_[lang]

def sex_view(filter, lang):
    if filter['f_filter']['type'] == 0:
        return lb.rooms_constr[lang]
    sex = filter['f_filter']['sex']
    if sex == 0:
        return lb.both[lang]
    elif sex == 1:
        return lb.male[lang]
    elif sex == 2:
        return lb.female[lang]
    elif sex == 3:
        return lb.couple[lang]
    else:
        return lb.none_[lang]

def pets_view(filter, lang):
    if filter['f_filter']['type'] == 0:
        return lb.rooms_constr[lang]
    pets = filter['f_filter']['pets']
    if pets:
        return lb.yes[lang]
    else:
        return lb.no[lang]

def smoke_view(filter, lang):
    if filter['f_filter']['type'] == 0:
        return lb.rooms_constr[lang]
    smoke = filter['f_filter']['smoke']
    if smoke:
        return lb.yes[lang]
    else:
        return lb.no[lang]

def owner_view(owner, lang):
    if owner:
        return lb.yes[lang]
    else:
        return lb.no[lang]

def filter_from_memory(filter, db, run_filter, lang):
    if run_filter:
        run_filter = ''
    else:
        run_filter = f'\n\n{lb.run_search_constr[lang]}'

    return f'''
{lb.filter[lang]} - "*{filter['name']}*"
{f_type_from_memory(filter, lang, main_view=True)}

*{lb.price[lang]}:*
{price_view(filter['f_filter']['min_price'],
             filter['f_filter']['max_price'], lang)}

{f_loc_from_memory(filter, db, lang, main_view=True)}

{f_other_from_memory(filter, lang, main_view=True)}{run_filter}'''

def f_loc_from_memory(filter, db, lang, main_view=False):
    up = '' if main_view else f'{lb.current_settings[lang]}\n'
    return f'''{up}*{lb.location[lang]}:*
{lb.city[lang]} - *{city_view(filter['f_filter']['city'],
                   db, lang)}*
{lb.district[lang]} - *{district_view(filter['f_filter'],
                           db, lang)}*
{lb.public_transport[lang]} - *{route_view(filter['g_filter']['route'],
                                db, lang)}*
{lb.distance_to_stop[lang]} - *{radius_view(filter['g_filter']['radius'], lang)}*'''

def f_type_from_memory(filter, lang, main_view=False):
    up = '' if main_view else f'{lb.current_settings[lang]}\n'
    return f'''{up}*{lb.property_type[lang]}:*
{lb.type_[lang]} - *{type_view(filter['f_filter']['type'], lang)}*
{lb.rooms[lang]} - *{rooms_view(filter, lang)}*'''

def f_other_from_memory(filter, lang, main_view=False):
    up = '' if main_view else f'{lb.current_settings[lang]}\n'
    return f'''{up}*{lb.other[lang]}:*
{lb.gender[lang]} - *{sex_view(filter, lang)}*
{lb.pets[lang]} - *{pets_view(filter, lang)}*
{lb.smoking[lang]} - *{smoke_view(filter, lang)}*
{lb.landlord[lang]} - *{owner_view(filter['f_filter']['owner'], lang)}*'''
