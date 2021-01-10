
import backend.general.mockups as mockups

async def donation(args=None, lang='en'):
    return [mockups.donation_start(lang),
            mockups.donation_keyboard(lang, 'main_menu-')]


async def lang_select(args=None, lang='en'):
    return [mockups.lang_select_text(lang),
            mockups.lang_select_keyboard(lang)]
async def main_menu(args=None, lang='en'):
    args.state.delete_user_filter(args.user_id)
    return [mockups.main_menu_text(lang),
            mockups.main_menu_keyboard(lang)]
async def empty_result(args=None, lang='en'):
    return [mockups.empty_result(lang),
            mockups.back_menu_keyboard(lang)]
async def f_error(args=None, lang='en'):
    return [mockups.f_error_text(lang),
            mockups.back_menu_keyboard(lang)]
