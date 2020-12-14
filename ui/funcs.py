
import ui.mockups as mockups
import ui.lang as l
from db.asql import get_user_filters
from db.asql import get_filter_by_ids
from db.asql import get_property_item
from ui.utils import build_page_keyboard
from ui.utils import build_common_keyboard
import mockups.filter as filter_view
from mockups.item import item_to_ui
from utils.filters_api import delete_filter
from utils.filters_api import send_show_more
from filters.compose import add_filter




async def user_filters(args, lang='en'):
    filters = await get_user_filters(args.pool, args.user_id)
    filters = [[x['name'], x['id']] for x in filters]
    buttons = [[l.main_menu[lang], 'main_menu-']]
    if filters:
        text = mockups.user_filters_text_filled(lang)
    else:
        text = mockups.user_filters_text_none(lang)
    return [text,
            build_common_keyboard(filters,
                                  'u_select',
                                  buttons)]

async def select_filter(args, lang='en'):
    filter = await get_filter_by_ids(args.pool,
                                     args.user_id,
                                     args.callback_data)
    await add_filter(args.state,
                     args.user_id,
                     filter[0])
    buttons = [[l.show_more_results[lang], f'show_more-{args.callback_data}'],
               ['Change Filter', f'change_filter-{args.callback_data}'],
               [l.delete_filter[lang], f'del_filter-{args.callback_data}'],
               [l.back[lang], 'user_filters-']]
    return [filter_view.filter_from_memory(args.state.filters[args.user_id],
                                           args.db),
            build_common_keyboard(None,
                                  None,
                                  buttons,
                                  in_row=False)]

async def change_user_filter(args, lang='en'):
    filter = await get_filter_by_ids(args.pool,
                                     args.user_id,
                                     args.callback_data)
    await add_filter(args.state,
                     args.user_id,
                     filter[0])
    return f_view(args,
                  lang=lang)

async def delete_user_filter(args, lang='en'):
    await delete_filter(int(args.callback_data))
    return await user_filters(args, lang=lang)

def lang_select(args=None, lang='en'):
    return [mockups.lang_select_text(lang),
            mockups.lang_select_keyboard(lang)]
def main_menu(args=None, lang='en'):
    args.state.delete_user_filter(args.user_id)
    return [mockups.main_menu_text(lang),
            mockups.main_menu_keyboard(lang)]

def f_view(args=None, lang='en'):
    filter = args.state.filters[args.user_id]
    current_filter = filter['id']
    return [filter_view.filter_from_memory(filter, args.db),
            mockups.f_view_keyboard(current_filter, lang)]

def f_loc_m(args=None, lang='en'):
    filter = args.state.filters[args.user_id]
    return [filter_view.f_loc_from_memory(filter, args.db),
            mockups.f_loc_m_keyboard(lang)]

def f_type_m(args=None, lang='en'):
    filter = args.state.filters[args.user_id]
    if filter['f_filter']['type'] == 1:
        rooms = False
    else:
        rooms = True
    return [filter_view.f_type_from_memory(filter),
            mockups.f_type_m_keyboard(rooms, lang)]

def f_other_m(args=None, lang='en'):
    filter = args.state.filters[args.user_id]
    if filter['f_filter']['type'] == 0:
        rooms = False
    else:
        rooms = True
    return [filter_view.f_other_from_memory(filter),
            mockups.f_other_m_keyboard(rooms, lang)]


def f_type(args=None, lang='en'):
    return [mockups.f_type_text(lang),
            mockups.f_type_keyboard(lang)]
def f_rooms(args=None, lang='en'):
    return [mockups.f_rooms_text(lang),
            mockups.f_rooms_keyboard(lang)]
def f_price(args=None, lang='en'):
    return [mockups.f_price_text(lang),
            mockups.f_price_keyboard(lang)]
def f_district(args, lang='en'):
    return [mockups.f_district_text(lang),
            build_page_keyboard(args.db.districts,
                                args.page,
                               'f_district',
                               'f_district',
                                back_callback='f_loc_m',
                                none_button=True,
                                lang=lang)]
def f_route_type(args=None, lang='en'):
    return [mockups.f_route_type_text(lang),
            mockups.f_route_type_keyboard(lang)]

def f_routes_metro(args, lang='en'):
    return [mockups.f_routes_metro(lang),
            build_page_keyboard(args.db.metro_routes,
                                args.page,
                               'f_route',
                               'f_routes_metro',
                                back_callback='f_route_type',
                                none_button=True,
                                lang=lang)]

def f_routes_bus(args, lang='en'):
    return [mockups.f_routes_bus(lang),
            build_page_keyboard(args.db.bus_routes,
                                args.page,
                               'f_route',
                               'f_routes_bus',
                                back_callback='f_route_type',
                                none_button=True,
                                lang=lang)]

def f_radius(args=None, lang='en'):
    return [mockups.f_radius_text(lang),
            mockups.f_radius_keyboard(lang)]

def f_sex(args=None, lang='en'):
    return [mockups.f_sex_text(lang),
            mockups.f_sex_keyboard(lang)]
def f_pets(args=None, lang='en'):
    return [mockups.f_pets_text(lang),
            mockups.f_pets_keyboard(lang)]
def f_smoke(args=None, lang='en'):
    return [mockups.f_smoke_text(lang),
            mockups.f_smoke_keyboard(lang)]
def f_owner(args=None, lang='en'):
    return [mockups.f_owner_text(lang),
            mockups.f_owner_keyboard(lang)]
def f_name(args=None, lang='en'):
    return [mockups.f_name_text(lang),
            mockups.f_name_keyboard(lang)]
# todo
def f_end(args=None, lang='en'):
    return [mockups.f_end_text(lang),
            mockups.back_menu_keyboard(lang)]
def f_name_type(args=None, lang='en'):
    text = mockups.f_name_type(lang)
    if args.callback_data is False:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_rooms_type(args=None, lang='en'):
    text = mockups.f_rooms_type(lang)
    if args.callback_data is False:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_price_type(args=None, lang='en'):
    text = mockups.f_price_type(lang)
    if args.callback_data is False:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
def f_error(args=None, lang='en'):
    return [mockups.f_error_text(lang),
            mockups.back_menu_keyboard(lang)]