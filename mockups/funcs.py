

import mockups.property as mockups
import ui.lang as l
from ui.utils import build_page_keyboard

async def title(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_title')
    text = mockups.u_title_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_title_keyboard(lang)]
async def description(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_desc')
    text = mockups.u_description_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_description_keyboard(lang)]
async def contact_name(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_contact')
    text = mockups.u_contact_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_contact_keyboard(lang)]
async def contact_phone(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_phone')
    text = mockups.u_phone_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_phone_keyboard(lang)]
async def photo(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_photo')
    text = mockups.u_photo_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_photo_keyboard(lang)]
async def type_(args=None, lang='en'):
    return [mockups.u_type_text(lang),
            mockups.u_type_keyboard(lang)]
async def rooms(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_rooms')
    text = mockups.u_rooms_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
            mockups.u_rooms_keyboard(lang)]
async def district(args=None, lang='en'):
    return [mockups.u_district_text(lang),
            build_page_keyboard(args.db.districts,
                                args.page,
                               'u_district',
                               'u_rooms',
                                back_callback='u_type',
                                lang=lang)]
async def price(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_price')
    text = mockups.u_price_text(lang)
    if args.error:
        text += l.direct_answer_err[lang]
    return [text,
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
