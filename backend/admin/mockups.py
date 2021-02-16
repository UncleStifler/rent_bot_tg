

from utils.utils import get_last_sec


def admin_text(lang='en'):
	return 'This is admin menu'


def admin_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'Обьявления пользователей', 'callback_data': 'a_show-'}],
		[{'text': 'Статистика', 'callback_data': 'a_stats-'}],
		[{'text': 'Рассылка', 'callback_data': 'a_mailing-'}],
		[{'text': 'Выйти из админки', 'callback_data': 'main_menu-'}],

	]}


def admin_statistics_text(a, b, c, d, e, lang='ru'):
	return 'Всего пользователей: {}\nАктивных пользователей ( за неделю ) : {}\n' \
		'Коэффициент фильтров на каждого пользователя: {}\nЧисло созданных объявлений через бот за прошлую ' \
		'неделю : {}\n Пользователей по языку интерфейса:\n Русский: {}\n Испанский: {}\n Английский: {}'.format(
		a, b, c, d, e[0], e[1], e[2])


def admin_statistics_keyboard(lang='ru'):
	return {'inline_keyboard': [
		[{'text': 'Назад', 'callback_data': 'a_main-'}]
	]}

def admin_mailing_main_text(lang='ru'):
	return 'Отправте мне то, что хотели разослать пользователям'


def admin_mailing_main_keyboard(lang='ru'):
	return {'inline_keyboard': [
		[{'text': 'Назад', 'callback_data': 'a_main-'}]
	]}


def admin_mailing_step2_keyboard(lang='ru'):
	return {'inline_keyboard': [
		[{'text': 'Изменить', 'callback_data': 'a_mailing-'}],
		[{'text': 'Продолжить', 'callback_data': 'a_mailing_step3-'}],
		[{'text': 'Назад', 'callback_data': 'a_main-'}]
	]}


def admin_mailing_step3_keyboard(lang='ru'):
	return {'inline_keyboard': [
		[{'text': '🇷🇺', 'callback_data': f'a_mailing_rus-'},
		 {'text': '🇺🇸', 'callback_data': f'a_mailing_en-'},
		 {'text': '🇪🇸', 'callback_data': f'a_mailing_es-'}],
		[{'text': 'Назад', 'callback_data': 'a_main-'}]
	]}


def admin_mailing_step4_keyboard(lang='ru'):
	return {'inline_keyboard': [
		[{'text': 'Изменить сообщение', 'callback_data': 'a_mailing-'}],
		[{'text': 'Изменить аудиторию', 'callback_data': 'a_mailing_step3-'}],
		[{'text': 'Опубликовать', 'callback_data': 'a_mailing_publish-'}],
		[{'text': 'Назад', 'callback_data': 'a_main-'}]
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
		[{'text': 'Back', 'callback_data': 'a_main_from_ad-'}]
	]}


def auth_text(lang='en'):
	return 'Type in the password'


def direct_answer_err(lang='en'):
	return f'\nInvalid Password ({get_last_sec()})'


