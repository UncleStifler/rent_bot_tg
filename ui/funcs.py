
import ui.mockups as mockups
from db.asql import get_user_filters
from db.asql import get_filter_by_ids
from db.asql import get_property_item
from ui.utils import build_page_keyboard
from ui.utils import build_common_keyboard
from mockups.filter import filter_to_ui
from mockups.item import item_to_ui
from utils.filters_api import delete_filter
from utils.filters_api import send_show_more


async def user_filters(user_id, pool, db, err=False):
    filters = await get_user_filters(pool, user_id)
    filters = [[x['name'], x['id']] for x in filters]
    buttons = [['Back to menu', 'main_menu-']]
    if filters:
        text = mockups.user_filters_text_filled
    else:
        text = mockups.user_filters_text_none
    if err:
        text = f'{mockups.f_error_text}{text}'
    return [text,
            build_common_keyboard(filters,
                                  'u_select',
                                  buttons)]

async def select_filter(user_id, pool, db, filter_id):
    filter = await get_filter_by_ids(pool, user_id,
                                     filter_id)
    buttons = [['Show results', f'show_more-{filter_id}'],
               ['Delete filter', f'del_filter-{filter_id}'],
               ['Back', 'user_filters-']]
    return [filter_to_ui(filter,
                         db),
            build_common_keyboard(None,
                                  None,
                                  buttons,
                                  in_row=False)]

async def delete_user_filter(user_id, pool, db, filter_id):
    try:
        await delete_filter(int(filter_id))
        return await user_filters(user_id, pool, db)
    except Exception as err:
        print(err)
        return await user_filters(user_id, pool, db, err=True)


def main_menu():
    return [mockups.main_menu_text,
            mockups.main_menu_keyboard]
def f_type():
    return [mockups.f_type_text,
            mockups.f_type_keyboard]
def f_rooms():
    return [mockups.f_rooms_text,
            mockups.f_rooms_keyboard]
def f_price():
    return [mockups.f_price_text,
            mockups.f_price_keyboard]
def f_district(db, page):
    return [mockups.f_district_text,
            build_page_keyboard(db.districts,
                                page,
                               'f_district',
                               'f_price')]
def f_route_type():
    return [mockups.f_route_type_text,
            mockups.f_route_type_keyboard]

def f_routes_metro(db, page):
    return [mockups.f_routes_metro,
            build_page_keyboard(db.metro_routes,
                                page,
                               'f_route',
                               'f_routes_metro',
                                skip=False)]

def f_routes_bus(db, page):
    return [mockups.f_routes_bus,
            build_page_keyboard(db.bus_routes,
                                page,
                               'f_route',
                               'f_routes_bus',
                                skip=False)]

def f_radius():
    return [mockups.f_radius_text,
            mockups.f_radius_keyboard]

def f_sex():
    return [mockups.f_sex_text,
            mockups.f_sex_keyboard]
def f_pets():
    return [mockups.f_pets_text,
            mockups.f_pets_keyboard]
def f_smoke():
    return [mockups.f_smoke_text,
            mockups.f_smoke_keyboard]
def f_owner():
    return [mockups.f_owner_text,
            mockups.f_owner_keyboard]
def f_name():
    return [mockups.f_name_text,
            mockups.f_name_keyboard]
def f_end():
    return [mockups.f_end_text,
            mockups.f_end_keyboard]
def f_name_type(err=False):
    text = mockups.f_name_type
    if err:
        text += mockups.direct_answer_err
    return [text,
            None]
def f_rooms_type(err=False):
    text = mockups.f_rooms_type
    if err:
        text += mockups.direct_answer_err
    return [text,
            None]
def f_price_type(err=False):
    text = mockups.f_price_type
    if err:
        text += mockups.direct_answer_err
    return [text,
            None]
def f_error():
    return [mockups.f_error_text,
            mockups.f_error_keyboard]