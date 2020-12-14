

import mockups.property as mockups

async def title(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_title')
    return [mockups.u_title_text(lang),
            None]
async def description(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_desc')
    return [mockups.u_description_text(lang),
            None]
async def contact_name(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_contact')
    return [mockups.u_contact_text(lang),
            None]
async def contact_phone(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_phone')
    return [mockups.u_phone_text(lang),
            None]
async def photo(args=None, lang='en'):
    await args.state.change_state(args.user_id, 'u_photo')
    return [mockups.u_photo_text(lang),
            None]
async def type_(args=None, lang='en'):
    return [mockups.u_type_text(lang),
            mockups.u_type_keyboard(lang)]
async def rooms(args=None, lang='en'):
    return [mockups.u_rooms_text(lang),
            mockups.u_rooms_keyboard(lang)]
async def district(args=None, lang='en'):
    # todo
    return [mockups.u_district_text(lang),
            None]
async def price(args=None, lang='en'):
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
