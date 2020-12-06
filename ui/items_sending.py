
from db.asql import get_property_item
from mockups.item import item_to_ui
from ui.utils import build_common_keyboard
from utils.tg_api import send_message

async def get_item_from_db(data, pool, db):
    filter_id = data['filter_id']
    property_id = data['property_id']
    item = await get_property_item(pool, filter_id, property_id)
    print(item)
    if not item:
        return None, None, None
    user_id = item[0]['user_id']
    url = item[0]['url']
    text = item_to_ui(db, item[0])
    # todo change callback to main menu
    buttons = [['Main menu', 'main_menu-'],
               ['Show more', f'show_more-{filter_id}']]
    keyboard = build_common_keyboard(None,
                                     None,
                                     buttons)
    if url:
        keyboard['inline_keyboard'].insert(0,
                                           [{'text': 'See on website',
                                             'url': url}])
    return [user_id,
            text,
            keyboard]

async def process_from_filter_app(data, pool, db):
    user_id, text, keyboard = await get_item_from_db(data, pool, db)
    if user_id:
        await send_message(user_id,
                           text,
                           keyboard)