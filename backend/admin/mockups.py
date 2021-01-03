

from utils.utils import get_last_sec


def admin_text(lang='en'):
	return 'This is admin menu'
def admin_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'Show users ad', 'callback_data': 'a_show-'}],
		[{'text': 'Main menu', 'callback_data': 'main_menu-'}]
	]}

def no_ads_text(lang='en'):
	return 'No ads in database'
def no_ads_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'Back', 'callback_data': 'a_main-'}],
		[{'text': 'Main menu', 'callback_data': 'main_menu-'}]
	]}
def ad_keyboard(ad_id, lang='en'):
	return {'inline_keyboard': [
		[{'text': 'Decline', 'callback_data': f'a_decline-{ad_id}'},
		 {'text': 'Accept', 'callback_data': f'a_accept-{ad_id}'}],
		[{'text': 'Back', 'callback_data': 'a_main-'}]
	]}

def auth_text(lang='en'):
	return 'Type in the password'

def direct_answer_err(lang='en'):
	return f'\nInvalid Password ({get_last_sec()})'


