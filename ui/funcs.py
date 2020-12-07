
import ui.mockups as mockups
import ui.lang as l
from db.asql import get_user_filters
from db.asql import get_filter_by_ids
from db.asql import get_property_item
from ui.utils import build_page_keyboard
from ui.utils import build_common_keyboard
from mockups.filter import filter_to_ui
from mockups.item import item_to_ui
from utils.filters_api import delete_filter
from utils.filters_api import send_show_more


async def user_filters(user_id, pool, db, lang='en', err=False):
    filters = await get_user_filters(pool, user_id)
    filters = [[x['name'], x['id']] for x in filters]
    buttons = [[l.main_menu[lang], 'main_menu-']]
    if filters:
        text = mockups.user_filters_text_filled(lang)
    else:
        text = mockups.user_filters_text_none(lang)
    if err:
        text = f'{mockups.f_error_text}{text}'
    return [text,
            build_common_keyboard(filters,
                                  'u_select',
                                  buttons)]

async def select_filter(user_id, pool, db, filter_id, lang='en'):
    filter = await get_filter_by_ids(pool,
                                     user_id,
                                     filter_id)
    buttons = [[l.show_more_results[lang], f'show_more-{filter_id}'],
               [l.delete_filter[lang], f'del_filter-{filter_id}'],
               [l.back[lang], 'user_filters-']]
    return [filter_to_ui(filter,
                         db),
            build_common_keyboard(None,
                                  None,
                                  buttons,
                                  in_row=False)]

async def delete_user_filter(user_id, pool, db, filter_id, lang='en'):
    try:
        await delete_filter(int(filter_id))
        return await user_filters(user_id, pool, db, lang=lang)
    except Exception as err:
        print(err)
        return await user_filters(user_id, pool, db, lang=lang, err=True)

def lang_select(lang='en'):
    return [mockups.lang_select_text(lang),
            mockups.lang_select_keyboard(lang)]
def main_menu(lang='en'):
    return [mockups.main_menu_text(lang),
            mockups.main_menu_keyboard(lang)]
def f_type(lang='en'):
    return [mockups.f_type_text(lang),
            mockups.f_type_keyboard(lang)]
def f_rooms(lang='en'):
    return [mockups.f_rooms_text(lang),
            mockups.f_rooms_keyboard(lang)]
def f_price(lang='en'):
    return [mockups.f_price_text(lang),
            mockups.f_price_keyboard(lang)]
def f_district(db, page, lang='en'):
    return [mockups.f_district_text(lang),
            build_page_keyboard(db.districts,
                                page,
                               'f_district',
                               'f_price',
                                lang)]
def f_route_type(lang='en'):
    return [mockups.f_route_type_text(lang),
            mockups.f_route_type_keyboard(lang)]

def f_routes_metro(db, page, lang='en'):
    return [mockups.f_routes_metro(lang),
            build_page_keyboard(db.metro_routes,
                                page,
                               'f_route',
                               'f_routes_metro',
                                lang,
                                skip=False)]

def f_routes_bus(db, page, lang='en'):
    return [mockups.f_routes_bus(lang),
            build_page_keyboard(db.bus_routes,
                                page,
                               'f_route',
                               'f_routes_bus',
                                lang,
                                skip=False)]

def f_radius(lang='en'):
    return [mockups.f_radius_text(lang),
            mockups.f_radius_keyboard(lang)]

def f_sex(lang='en'):
    return [mockups.f_sex_text(lang),
            mockups.f_sex_keyboard(lang)]
def f_pets(lang='en'):
    return [mockups.f_pets_text(lang),
            mockups.f_pets_keyboard(lang)]
def f_smoke(lang='en'):
    return [mockups.f_smoke_text(lang),
            mockups.f_smoke_keyboard(lang)]
def f_owner(lang='en'):
    return [mockups.f_owner_text(lang),
            mockups.f_owner_keyboard(lang)]
def f_name(lang='en'):
    return [mockups.f_name_text(lang),
            mockups.f_name_keyboard(lang)]
def f_end(lang='en'):
    return [mockups.f_end_text(lang),
            mockups.back_menu_keyboard(lang)]
def f_name_type(err=False, lang='en'):
    text = mockups.f_name_type(lang)
    if err:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_rooms_type(err=False, lang='en'):
    text = mockups.f_rooms_type(lang)
    if err:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_price_type(err=False, lang='en'):
    text = mockups.f_price_type(lang)
    if err:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_error(lang='en'):
    return [mockups.f_error_text(lang),
            mockups.back_menu_keyboard(lang)]