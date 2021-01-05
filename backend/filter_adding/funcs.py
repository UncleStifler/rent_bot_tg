
import backend.filter_adding.mockups as mockups

import ui.lang_buttons as lb
from db.asql import get_user_filters
from db.asql import get_filter_by_ids
from ui.utils import build_page_keyboard
from ui.utils import build_common_keyboard
import backend.filter_adding.view as filter_view
from utils.filters_api import delete_filter
from backend.filter_adding.filter_composing import add_filter




async def user_filters(args, lang='en'):
    filters = await get_user_filters(args.pool, args.user_id)
    filters = [[x['name'], x['id']] for x in filters]
    buttons = [[lb.main_menu[lang], 'main_menu-']]
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
    buttons = [[lb.show_more_results[lang], f'show_more-{args.callback_data}'],
               [lb.change_filter[lang], f'change_filter-{args.callback_data}'],
               [lb.delete_filter[lang], f'del_filter-{args.callback_data}'],
               [lb.back[lang], 'user_filters-']]
    return [filter_view.filter_from_memory(args.state.filters[args.user_id],
                                           args.db, True, lang),
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
    return await f_view(args,
                  lang=lang)

async def delete_user_filter(args, lang='en'):
    await delete_filter(int(args.callback_data))
    return await user_filters(args, lang=lang)




async def f_view(args=None, lang='en'):
    await args.state.change_state(args.user_id, None)
    filter = args.state.filters[args.user_id]
    current_filter = filter['id']
    run_filter = filter['f_filter']['city'] or filter['f_filter']['min_price'] or filter['f_filter']['max_price']
    return [filter_view.filter_from_memory(filter, args.db, run_filter, lang),
            mockups.f_view_keyboard(current_filter, run_filter, lang)]

async def f_loc_m(args=None, lang='en', districts=False):
    filter = args.state.filters[args.user_id]
    if filter['f_filter']['city']:
        districts = True
    return [filter_view.f_loc_from_memory(filter, args.db, lang),
            mockups.f_loc_m_keyboard(districts, lang)]

async def f_type_m(args=None, lang='en', rooms=True):
    filter = args.state.filters[args.user_id]
    if filter['f_filter']['type'] == 1:
        rooms = False
    return [filter_view.f_type_from_memory(filter, lang),
            mockups.f_type_m_keyboard(rooms, lang)]

async def f_other_m(args=None, lang='en'):
    filter = args.state.filters[args.user_id]
    if filter['f_filter']['type'] == 0:
        rooms = False
    else:
        rooms = True
    return [filter_view.f_other_from_memory(filter, lang),
            mockups.f_other_m_keyboard(rooms, lang)]


async def f_type(args=None, lang='en'):
    return [mockups.f_type_text(lang),
            mockups.f_type_keyboard(lang)]
async def f_rooms(args=None, lang='en'):
    return [mockups.f_rooms_text(lang),
            mockups.f_rooms_keyboard(lang)]
async def f_price(args=None, lang='en'):
    return [mockups.f_price_text(lang),
            mockups.f_price_keyboard(lang)]
async def f_city(args, lang='en'):
    return [mockups.f_city_text(lang),
            build_page_keyboard(args.db.cities,
                                args.page,
                               'f_city',
                               'f_city',
                                back_callback='f_loc_m',
                                none_button=True,
                                lang=lang)]
async def f_district(args, lang='en'):
    city = args.state.filters[args.user_id]['f_filter']['city']
    return [mockups.f_district_text(lang),
            build_page_keyboard(args.db.get_districts(city),
                                args.page,
                               'f_district',
                               'f_district',
                                back_callback='f_loc_m',
                                none_button=True,
                                lang=lang)]
async def f_route_type(args=None, lang='en'):
    return [mockups.f_route_type_text(lang),
            mockups.f_route_type_keyboard(lang)]

async def f_routes_metro(args, lang='en'):
    return [mockups.f_routes_metro(lang),
            build_page_keyboard(args.db.metro_routes,
                                args.page,
                               'f_route',
                               'f_routes_metro',
                                back_callback='f_route_type',
                                none_button=True,
                                lang=lang)]

async def f_routes_bus(args, lang='en'):
    return [mockups.f_routes_bus(lang),
            build_page_keyboard(args.db.bus_routes,
                                args.page,
                               'f_route',
                               'f_routes_bus',
                                back_callback='f_route_type',
                                none_button=True,
                                lang=lang)]

async def f_routes_trains(args, lang='en'):
    return [mockups.f_routes_train(lang),
            build_page_keyboard(args.db.trains,
                                args.page,
                               'f_route',
                               'f_routes_trains',
                                back_callback='f_route_type',
                                none_button=True,
                                lang=lang)]

async def f_radius(args=None, lang='en'):
    return [mockups.f_radius_text(lang),
            mockups.f_radius_keyboard(lang)]

async def f_sex(args=None, lang='en'):
    return [mockups.f_sex_text(lang),
            mockups.f_sex_keyboard(lang)]
async def f_pets(args=None, lang='en'):
    return [mockups.f_pets_text(lang),
            mockups.f_pets_keyboard(lang)]
async def f_smoke(args=None, lang='en'):
    return [mockups.f_smoke_text(lang),
            mockups.f_smoke_keyboard(lang)]
async def f_owner(args=None, lang='en'):
    return [mockups.f_owner_text(lang),
            mockups.f_owner_keyboard(lang)]
async def f_name(args=None, lang='en'):
    return [mockups.f_name_text(lang),
            mockups.f_name_keyboard(lang)]
# todo sending menu after ending
async def f_end(args=None, lang='en'):
    return [mockups.f_end_text(lang),
            mockups.back_menu_keyboard(lang)]
async def f_name_type(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'f_name_type')
    text = mockups.f_name_type(lang)
    if args.error:
        text += mockups.direct_answer_err(lang)
    return [text,
            mockups.back_to_f_view(lang)]
async def f_rooms_type(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'f_rooms_type')
    text = mockups.f_rooms_type(lang)
    if args.error:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
async def f_price_type(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'f_price_type')
    text = mockups.f_price_type(lang)
    if args.error:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]
