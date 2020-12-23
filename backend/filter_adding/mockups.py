
import ui.lang as l
from utils.utils import get_last_sec
# main menu

def main_menu_text(lang='en'):
	return l.main_menu_text[lang]

def main_menu_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': l.add_filter[lang], 'callback_data': 'f_start-'}],
		[{'text': l.my_filters[lang], 'callback_data': 'user_filters-'}],
		[{'text': 'Add property', 'callback_data': 'u_start_page-'}],
		[{'text': l.select_lang[lang], 'callback_data': 'select_lang-'}]
	]}

def user_filters_text_filled(lang='en'):
	return l.user_filters_text_filled[lang]
def user_filters_text_none(lang='en'):
	return l.user_filters_text_none[lang]

def lang_select_text(lang='en'):
	return l.lang_select[lang]
def lang_select_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'English', 'callback_data': 'lang-en'}],
		[{'text': 'Español', 'callback_data': 'lang-es'}],
		[{'text': 'Русский', 'callback_data': 'lang-ru'}]
	]}
###########################################################
def f_view_keyboard(current_filter=None, lang='en'):
	if current_filter:
		add = 'f_end_change-'
		back = f'u_select-{current_filter}'
	else:
		add = 'f_end-'
		back = 'main_menu-'
	return {'inline_keyboard': [
	[{'text': 'Run filter', 'callback_data': add}],
	[{'text': 'Change filter name', 'callback_data': 'f_name_type-'}],
	[{'text': 'Property Type', 'callback_data': 'f_type_m-'},
	 {'text': 'Location', 'callback_data': 'f_loc_m-'}],
	[{'text': 'Price', 'callback_data': 'f_price-'},
	 {'text': 'Other', 'callback_data': 'f_other_m-'}],
	[{'text': l.back[lang], 'callback_data': back}]
	]}
def f_loc_m_keyboard(districts, lang='en'):
	keyboard = {'inline_keyboard': [
	[{'text': 'City', 'callback_data': 'f_city-'}],
	[{'text': 'Public Transport', 'callback_data': 'f_route_type-'}],
	[{'text': 'Distance to stop', 'callback_data': 'f_radius-'}],
	[{'text': l.back[lang], 'callback_data': 'f_view-'}]
	]}
	if districts:
		keyboard['inline_keyboard'].insert(1, [{'text': 'District', 'callback_data': 'f_district-'}])
	return keyboard
def f_type_m_keyboard(rooms, lang='en'):
	keyboard = {'inline_keyboard': [
			[{'text': 'Type', 'callback_data': 'f_type-'}],
			[{'text': l.back[lang], 'callback_data': 'f_view-'}]
	]}
	if rooms:
		keyboard['inline_keyboard'].insert(1, [{'text': 'Rooms', 'callback_data': 'f_rooms-'}])
	return keyboard
def f_other_m_keyboard(rooms=True, lang='en'):
	if rooms:
		return {'inline_keyboard': [
		[{'text': 'Gender', 'callback_data': 'f_sex-'},
		 {'text': 'Pets', 'callback_data': 'f_pets-'}],
		[{'text': 'Smoke', 'callback_data': 'f_smoke-'},
		 {'text': 'Owner', 'callback_data': 'f_owner-'}],
		[{'text': l.back[lang], 'callback_data': 'f_view-'}]
		]}
	else:
		return {'inline_keyboard': [
			[{'text': 'Owner', 'callback_data': 'f_owner-'}],
			[{'text': l.back[lang], 'callback_data': 'f_view-'}]
		]}
###########################################################
def f_type_text(lang='en'):
	return l.f_type_text[lang]
def f_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.flat[lang], 'callback_data': 'f_type-0'},
	 {'text': l.room[lang], 'callback_data': 'f_type-1'}],
	[{'text': 'Both', 'callback_data': 'f_type-2'}],
	[{'text': l.back[lang], 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def f_rooms_text(lang='en'):
	return l.f_rooms_text[lang]
def f_rooms_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '1', 'callback_data': 'f_rooms-1'},
	{'text': '2', 'callback_data': 'f_rooms-2'},
	{'text': '3', 'callback_data': 'f_rooms-3'},
	 {'text': '4', 'callback_data': 'f_rooms-4'}],
	[{'text': l.type_in[lang], 'callback_data': 'f_rooms_type-'},
	 {'text': l.doesnt_matter[lang], 'callback_data': 'f_rooms-0'}],
	[{'text': l.back[lang], 'callback_data': 'f_type_m-'}]
	]}
def f_rooms_type(lang='en'):
	return l.f_rooms_type[lang]
###########################################################
def f_price_text(lang='en'):
	return l.f_price_text[lang]
def f_price_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '300-500', 'callback_data': 'f_price-300/500'},
	{'text': '500-700', 'callback_data': 'f_price-500/700'}],
	[{'text': '700-1000', 'callback_data': 'f_price-700/1000'},
	{'text': '> 1000', 'callback_data': 'f_price->1000'}],
	[{'text': l.type_in[lang], 'callback_data': 'f_price_type-'},
	 {'text': l.doesnt_matter[lang], 'callback_data': 'f_price-0'}],
	[{'text': l.back[lang], 'callback_data': 'f_view-'}]
	]}
def f_price_type(lang='en'):
	return l.f_price_type[lang]
###########################################################
def f_city_text(lang='en'):
	return 'City choice'
###########################################################
def f_district_text(lang='en'):
	return l.f_district_text[lang]
###########################################################
def f_route_type_text(lang='en'):
	return l.f_route_type_text[lang]
def f_route_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.metro[lang], 'callback_data': 'f_routes_metro-'},
	 {'text': l.bus[lang], 'callback_data': 'f_routes_bus-'}],
	[{'text': l.back[lang], 'callback_data': 'f_loc_m-'}]
	]}
###########################################################
def f_routes_bus(lang='en'):
	return l.f_routes_bus[lang]
###########################################################
def f_routes_metro(lang='en'):
	return l.f_routes_metro[lang]
###########################################################
def f_radius_text(lang='en'):
	return l.f_radius_text[lang]
def f_radius_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '300 m', 'callback_data': 'f_radius-0.3'},
	 {'text': '500 m', 'callback_data': 'f_radius-0.5'}],
	[{'text': '1 km', 'callback_data': 'f_radius-1'},
	 {'text': '2 km', 'callback_data': 'f_radius-2'}],
	[{'text': l.back[lang], 'callback_data': 'f_loc_m-'}]
	]}
###########################################################
def f_sex_text(lang='en'):
	return l.f_sex_text[lang]
def f_sex_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.male[lang], 'callback_data': 'f_sex-1'},
	 {'text': l.female[lang], 'callback_data': 'f_sex-2'}],
	[{'text': 'Couple', 'callback_data': 'f_sex-3'}],
	[{'text': l.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_pets_text(lang='en'):
	return l.f_pets_text[lang]
def f_pets_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.yes[lang], 'callback_data': 'f_pets-1'},
	 {'text': l.no[lang], 'callback_data': 'f_pets-0'}],
	[{'text': l.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_smoke_text(lang='en'):
	return l.f_smoke_text[lang]
def f_smoke_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.yes[lang], 'callback_data': 'f_smoke-1'},
	 {'text': l.no[lang], 'callback_data': 'f_smoke-0'}],
	[{'text': l.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_owner_text(lang='en'):
	return l.f_owner_text[lang]
def f_owner_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.yes[lang], 'callback_data': 'f_owner-1'},
	 {'text': l.no[lang], 'callback_data': 'f_owner-0'}],
	[{'text': l.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_name_text(lang='en'):
	return l.f_name_text[lang]
def f_name_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.type_in[lang], 'callback_data': 'f_name_type-'}],
	[{'text': l.leave_default[lang], 'callback_data': 'f_end-'}]
	]}
def f_name_type(lang='en'):
	return l.f_name_type[lang]
###########################################################
def f_end_text(lang='en'):
	return l.f_end_text[lang]

def direct_answer_err(lang='en'):
	return f'\n{l.direct_answer_err[lang]} ({get_last_sec()})'
def f_error_text(lang='en'):
	return l.f_error_text[lang]
def back_menu_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': l.main_menu[lang], 'callback_data': 'main_menu-'}]
	]}

