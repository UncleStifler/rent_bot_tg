

from utils.utils import get_last_sec


def admin_text(lang='en'):
	return 'This is admin menu'
def admin_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'Show users ad', 'callback_data': 'a_show-'}],
		[{'text': 'Main menu', 'callback_data': 'main_menu-'}]
	]}


def auth_text(lang='en'):
	return 'Type in the password'

def direct_answer_err(lang='en'):
	return f'\nInvalid Password ({get_last_sec()})'


