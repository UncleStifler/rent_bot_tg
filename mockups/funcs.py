

import mockups.property as mockups
from ui.utils import build_page_keyboard

async def title(args=None, lang='en'):
    print('title called')
    await args.state.change_state(args.user_id, 'u_title')
    return [mockups.u_title_text(lang),
            mockups.u_title_keyboard(lang)]
async def description(args=None, lang='en'):
    print('descr called')
    await args.state.change_state(args.user_id, 'u_desc')
    return [mockups.u_description_text(lang),
            mockups.u_description_keyboard(lang)]
async def contact_name(args=None, lang='en'):
    print('cont called')
    await args.state.change_state(args.user_id, 'u_contact')
    return [mockups.u_contact_text(lang),
            mockups.u_contact_keyboard(lang)]
async def contact_phone(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_phone')
    return [mockups.u_phone_text(lang),
            mockups.u_phone_keyboard(lang)]
async def photo(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_photo')
    return [mockups.u_photo_text(lang),
            mockups.u_photo_keyboard(lang)]
async def type_(args=None, lang='en'):
    return [mockups.u_type_text(lang),
            mockups.u_type_keyboard(lang)]
async def rooms(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_rooms')
    return [mockups.u_rooms_text(lang),
            mockups.u_rooms_keyboard(lang)]
async def district(args=None, lang='en'):
    # todo
    return [mockups.u_district_text(lang),
            build_page_keyboard(args.db.districts,
                                args.page,
                               'u_district',
                               'u_rooms',
                                back_callback='u_rooms',
                                lang=lang)]
async def price(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_price')
    return [mockups.u_price_text(lang),
            mockups.u_price_keyboard(lang)]
async def sex(args=None, lang='en'):
    return [mockups.u_sex_text(lang),
            mockups.u_sex_keyboard(lang)]
async def pets(args=None, lang='en'):
    return [mockups.u_pets_text(lang),
            mockups.u_pets_keyboard(lang)]
async def smoke(args=None, lang='en'):
    return [mockups.u_smoke_text(lang),
            mockups.u_smoke_keyboard(lang)]
async def owner(args=None, lang='en'):
    return [mockups.u_owner_text(lang),
            mockups.u_owner_keyboard(lang)]
