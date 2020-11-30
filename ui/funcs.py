
import ui.mockups as mockups
from db.asql import get_user_filters
from db.asql import get_filter_by_ids
from ui.utils import build_page_keyboard
from ui.utils import build_common_keyboard
from ui.utils import filter_to_ui


async def user_filters(user_id, pool):
    filters = await get_user_filters(pool, user_id)
    filters = [[x['name'], x['id']] for x in filters]
    if filters:
        return [mockups.user_filters_text_filled,
                build_common_keyboard(filters,
                                      'u_select',
                                      'Back to menu',
                                      'main_menu')]
    else:
        return [mockups.user_filters_text_none,
                build_common_keyboard(None,
                                      None,
                                      'Back to menu',
                                      'main_menu')]

async def select_filter(bd, user_id, filter_id, pool):
    filter = await get_filter_by_ids(pool, user_id,
                                     filter_id)
    return [filter_to_ui(filter,
                         bd),
            build_common_keyboard(None,
                                  None,
                                  'Back',
                                  'user_filters')]



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