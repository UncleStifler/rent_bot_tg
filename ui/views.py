

import ui.lang_buttons as lb
from ui.utils import search_bd

def type_view(type, lang, return_none=False):
    if type is None:
        if return_none:
            return lb.both[lang]
    elif type == 0:
        return lb.flat[lang]
    elif type == 1:
        return lb.room[lang]

def city_view(city, db, lang, return_none=False):
    if not city:
        if return_none:
            return lb.none_[lang]
    else:
        return search_bd(city, db.cities)

def district_view(district, db, lang, return_none=False):
    if not district:
        if return_none:
            return lb.none_[lang]
    else:
        return search_bd(district, db.districts)

def sex_view(sex, lang, return_none=False):
    if sex == 0:
        return lb.both[lang]
    elif sex == 1:
        return lb.male[lang]
    elif sex == 2:
        return lb.female[lang]
    elif sex == 3:
        return lb.couple[lang]
    else:
        if return_none:
            return lb.none_[lang]

def owner_view(owner, lang, return_none=False):
    if owner:
        return lb.landlord_botton[lang]
    else:
        if owner is False:
            return lb.agent_botton[lang]
        if owner is None:
            if return_none:
                return lb.agent_botton[lang]

def yes_or_no(parameter, lang):
    if parameter:
        return lb.yes[lang]
    else:
        if parameter is False:
            return lb.no[lang]