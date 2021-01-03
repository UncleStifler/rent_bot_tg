
import backend.admin.mockups as mockups
from db.asql import (get_last_user_ad,
                     delete_user_ad,
                     insert_user_ad_to_db)
from backend.admin.utils import get_ad_text
from utils.filters_api import send_new_ids

async def admin(args=None, lang='en'):
    return [mockups.admin_text(lang),
            mockups.admin_keyboard(lang)]


async def admin_auth(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'a_auth')
    text = mockups.auth_text(lang)
    if args.error:
        text += mockups.direct_answer_err(lang)
    return [text,
            None]

async def show_last_ad(args=None, lang='en'):
    data = await get_last_user_ad(args.pool)
    if data:
        id_, text = get_ad_text(data[0], args.db, lang)
        return [text,
                mockups.ad_keyboard(id_, lang)]
    else:
        return [mockups.no_ads_text(lang),
                mockups.no_ads_keyboard(lang)]

async def decline_ad(args=None, lang='en'):
    await delete_user_ad(args.pool, args.callback_data)
    return await show_last_ad(args, lang)

async def accept_ad(args=None, lang='en'):
    id_ = await insert_user_ad_to_db(args.pool, args.callback_data)
    await delete_user_ad(args.pool, args.callback_data)
    await send_new_ids(id_)
    return await show_last_ad(args, lang)