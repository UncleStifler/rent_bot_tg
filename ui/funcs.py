
import ui.mockups as mockups
from ui.utils import build_keyboard


def f_end():
    return [mockups.f_end_text,
            mockups.f_end_keyboard]
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
            build_keyboard(db.districts,
                           page,
                           'f_district',
                           'f_price')]
def f_route_type():
    return [mockups.f_route_type_text,
            mockups.f_route_type_keyboard]

def f_routes_metro(db, page):
    return [mockups.f_routes_metro,
            build_keyboard(db.metro_routes,
                           page,
                           'f_route',
                           'f_routes_metro',
                           skip=False)]

def f_routes_bus(db, page):
    return [mockups.f_routes_bus,
            build_keyboard(db.bus_routes,
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