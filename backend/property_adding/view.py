
import ui.lang_lines as ll
import ui.lang_buttons as lb
from ui.utils import search_bd
from ui.utils import get_parameter
from backend.photos import get_photo_url

from ui.views import *

# city = search_bd(item['city'], db.cities)
# district = search_bd(item['district'], db.districts)





def ad_view(ad, db, text, lang):
    title = get_parameter(f'{lb.title[lang]} - *%s*\n', ad['description']['title'])
    description = get_parameter(f'{lb.description[lang]} - *%s*\n', ad['description']['description'])
    name = get_parameter(f'{lb.name[lang]} - *%s*\n', ad['description']['contact_name'])
    phone = get_parameter(f'{lb.phone[lang]} - *%s*\n', ad['description']['contact_phone'])
    # photo = get_parameter(f'{lb.photo[lang]} - *%s*\n', get_photo_url(ad['description']['photo']))
    type_ = get_parameter(f'{lb.type_one_word[lang]} - *%s*\n', type_view(ad['property']['type'], lang))
    rooms = get_parameter(f'{lb.rooms_number[lang]} - *%s*\n', ad['property']['rooms'])
    city = get_parameter(f'{lb.city[lang]} - *%s*\n', city_view(ad['property']['city'], db, lang))
    district = get_parameter(f'{lb.district[lang]} - *%s*\n', district_view(ad['property']['district'], db, lang))
    price = get_parameter(f'{lb.price[lang]} - *%s* €\n', ad['property']['price'])
    sex = get_parameter(f'{lb.gender[lang]} - *%s*\n', sex_view(ad['property']['sex'], lang))
    pets = get_parameter(f'{lb.pets[lang]} - *%s*\n', yes_or_no(ad['property']['pets'], lang))
    smoke = get_parameter(f'{lb.smoking[lang]} - *%s*\n', yes_or_no(ad['property']['smoke'], lang))
    owner = get_parameter(f'{lb.landlord[lang]} - *%s*\n', owner_view(ad['property']['owner'], lang))

    ad_preview = f'{title}{description}{name}{phone}{type_}{rooms}{city}{district}{price}{sex}{pets}{smoke}{owner}'
    return f'{ad_preview}\n{text}'
