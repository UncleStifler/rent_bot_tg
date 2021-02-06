
import backend.admin.mockups as mockups
from db.asql import (get_last_user_ad,
                     delete_user_ad,
                     insert_user_ad_to_db,
                     get_users,
                     get_a_users_ads_count,
                     get_a_filter_count,
                     get_a_active_users,
                     insert_post,
                     get_post,
                     delete_post)
from backend.admin.utils import get_ad_text
from utils.filters_api import send_new_ids
from backend.admin.posting import posting


async def admin(args=None, lang='en'):
    return [mockups.admin_text(lang),
            mockups.admin_keyboard(lang)]


async def admin_statistics(args=None, lang='ru'):
    a = await get_users(args.pool, lang=None)
    a = len(a)#str(a).split('=')[1].replace('>', '').replace(']', '')
    b = await get_a_active_users(args.pool)
    b = str(b).split('=')[1].replace('>', '').replace(']', '')
    c = await get_a_filter_count(args.pool)
    c = int(str(c).split('=')[1].replace('>', '').replace(']', ''))/int(a)
    d = await get_a_users_ads_count(args.pool)
    if str(d) == '[<Record count=0>]':
        d = 0
    else:
        d = len(d)

    e = [len(await get_users(args.pool, lang='ru')), len(await get_users(args.pool, lang='es')),
         len(await get_users(args.pool, lang='en'))]
    return [mockups.admin_statistics_text(a, b, round(c, 2), d, e, lang),
            mockups.admin_statistics_keyboard(lang)]

def mailing_(message):
    # insert_post_firstly(data=message)
    global post_text
    post_text = message
    return message


async def admin_mailing(args=None, lang='ru'):
    await args.state.change_state(args.user_id, 'a_mailing')
    return [mockups.admin_mailing_main_text(lang),
            mockups.admin_mailing_main_keyboard(lang)]

async def insert_post_firstly(args=None, data=None):
    return await insert_post(args.pool, data)

async def admin_inset_post(args=None, data=None, lang='ru'):
    await insert_post(args.pool, data)

async def admin_mailing_step2(args=None, lang='ru'):
    # await args.state.change_state(args.user_id, 'a_mailing')
    text = "Ваше сообщение: \n" + post_text
    return [text,
            mockups.admin_mailing_step2_keyboard(lang)]

async def admin_mailing_step3(args=None, lang='ru'):
    text = "Выберите аудиторию рассылки"
    return [text, mockups.admin_mailing_step3_keyboard(lang)]

async def admin_mailing_step4_ru(args=None, lang='ru'):
    text = "Ваше сообщение: \n" + post_text + "\nАудитория: 🇷🇺"
    await insert_post(args.pool, post_text, 'ru')
    return [text, mockups.admin_mailing_step4_keyboard(lang)]

async def admin_mailing_step4_en(args=None, lang='ru'):
    text = "Ваше сообщение: \n" + post_text + "\nАудитория: 🇺🇸"
    await insert_post(args.pool, post_text, 'en')
    return [text, mockups.admin_mailing_step4_keyboard(lang)]

async def admin_mailing_step4_es(args=None, lang='es'):
    text = "Ваше сообщение: \n" + post_text + "\nАудитория: 🇪🇸"
    return [text, mockups.admin_mailing_step4_keyboard(lang)]

async def admin_post_publish(args=None, lang='ru'):
    post = await get_post(args.pool)
    text = post[0]['post_text']
    lang = post[0]['lang']
    user_list = await get_users(args.pool, lang=lang)
    counter = 0
    for user in user_list:
        user = str(user).split('=')[1].replace('>', '').replace(']', '')
        r = posting(user, text)
        if r:
            counter += 1

    await delete_post(args.pool)
    return [f'Рассылка выполнена, всего {counter} сообщений', mockups.admin_keyboard()]


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