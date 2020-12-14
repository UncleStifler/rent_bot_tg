

import ui.lang as l
from db.asql import get_property_item
from ui.item_view import item_to_ui
from ui.utils import build_common_keyboard
from utils.tg_api import send_message

async def _get_item_from_db(data, pool, db, lang):
    filter_id = data['filter_id']
    property_id = data['property_id']
    item = await get_property_item(pool, filter_id, property_id)
    if not item:
        return None, None, None
    user_id = item[0]['user_id']
    url = item[0]['url']
    lat, lon = item[0]['latitude'], item[0]['longitude']
    lat_lon = f'map-{lat}|{lon}'
    text = item_to_ui(db, item[0])
    buttons = [[l.main_menu[lang], 'main_menu-'],
               [l.show_more_results[lang], f'show_more-{filter_id}']]
    keyboard = build_common_keyboard(None,
                                     None,
                                     buttons)
    keyboard['inline_keyboard'].insert(0,
                                       [{'text': l.see_website[lang],
                                         'url': url},
                                        {'text': l.see_map[lang],
                                         'callback_data': lat_lon}])
    return [user_id,
            text,
            keyboard]

async def process_from_filter_app(data, pool, db, user_state, lang='en'):
    user_id, text, keyboard = await _get_item_from_db(data, pool, db, lang=lang)
    if user_id:
        await user_state.change_message_id(user_id, None)
        await send_message(user_id,
                           text,
                           keyboard)