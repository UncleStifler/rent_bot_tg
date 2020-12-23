
import backend.admin.mockups as mockups


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
