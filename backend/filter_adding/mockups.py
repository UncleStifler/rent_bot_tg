
import ui.lang_lines as ll
import ui.lang_buttons as lb
from utils.utils import get_last_sec
# main menu

def main_menu_text(lang='en'):
	return ll.main_menu_text[lang]

def main_menu_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': lb.add_filter[lang], 'callback_data': 'f_start-'}],
		[{'text': lb.my_filters[lang], 'callback_data': 'user_filters-'}],
		[{'text': lb.add_property[lang], 'callback_data': 'u_start_page-'}],
		[{'text': lb.select_lang[lang], 'callback_data': 'select_lang-'}]
	]}

def empty_result(lang='en'):
	return ll.empty_results[lang]

def user_filters_text_filled(lang='en'):
	return ll.user_filters_text_filled[lang]
def user_filters_text_none(lang='en'):
	return ll.user_filters_text_none[lang]

def lang_select_text(lang='en'):
	return ll.lang_select[lang]
def lang_select_keyboard(lang='en'):
	return {'inline_keyboard': [
		[{'text': 'English', 'callback_data': 'lang-en'}],
		[{'text': 'Español', 'callback_data': 'lang-es'}],
		[{'text': 'Русский', 'callback_data': 'lang-ru'}]
	]}
###########################################################
def f_view_keyboard(current_filter=None, run_filter=False, lang='en'):
	if current_filter:
		add = 'f_end_change-'
		back = f'u_select-{current_filter}'
	else:
		add = 'f_end-'
		back = 'main_menu-'
	keyboard = {'inline_keyboard': [
	[{'text': lb.change_filter_name[lang], 'callback_data': 'f_name_type-'}],
	[{'text': lb.property_type[lang], 'callback_data': 'f_type_m-'},
	 {'text': lb.location[lang], 'callback_data': 'f_loc_m-'}],
	[{'text': lb.price[lang], 'callback_data': 'f_price-'},
	 {'text': lb.other[lang], 'callback_data': 'f_other_m-'}],
	[{'text': lb.back[lang], 'callback_data': back}]
	]}
	if run_filter:
		keyboard['inline_keyboard'].insert(0, [{'text': lb.finish_adding_filter[lang], 'callback_data': add}])
	return keyboard
def f_loc_m_keyboard(districts, lang='en'):
	keyboard = {'inline_keyboard': [
	[{'text': lb.city[lang], 'callback_data': 'f_city-'}],
	[{'text': lb.public_transport[lang], 'callback_data': 'f_route_type-'}],
	[{'text': lb.distance_to_stop[lang], 'callback_data': 'f_radius-'}],
	[{'text': lb.done[lang], 'callback_data': 'f_view-'}]
	]}
	if districts:
		keyboard['inline_keyboard'].insert(1, [{'text': lb.district[lang], 'callback_data': 'f_district-'}])
	return keyboard
def f_type_m_keyboard(rooms, lang='en'):
	keyboard = {'inline_keyboard': [
			[{'text': lb.type_[lang], 'callback_data': 'f_type-'}],
			[{'text': lb.done[lang], 'callback_data': 'f_view-'}]
	]}
	if rooms:
		keyboard['inline_keyboard'].insert(1, [{'text': lb.rooms_number[lang], 'callback_data': 'f_rooms-'}])
	return keyboard
def f_other_m_keyboard(rooms=True, lang='en'):
	if rooms:
		return {'inline_keyboard': [
		[{'text': lb.gender[lang], 'callback_data': 'f_sex-'},
		 {'text': lb.pets[lang], 'callback_data': 'f_pets-'}],
		[{'text': lb.smoking[lang], 'callback_data': 'f_smoke-'},
		 {'text': lb.landlord[lang], 'callback_data': 'f_owner-'}],
		[{'text': lb.done[lang], 'callback_data': 'f_view-'}]
		]}
	else:
		return {'inline_keyboard': [
			[{'text': lb.landlord[lang], 'callback_data': 'f_owner-'}],
			[{'text': lb.done[lang], 'callback_data': 'f_view-'}]
		]}
###########################################################
def f_type_text(lang='en'):
	return ll.f_type_text[lang]
def f_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.flat[lang], 'callback_data': 'f_type-0'},
	 {'text': lb.room[lang], 'callback_data': 'f_type-1'}],
	[{'text': lb.both[lang], 'callback_data': 'f_type-2'}],
	[{'text': lb.back[lang], 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def f_rooms_text(lang='en'):
	return ll.f_rooms_text[lang]
def f_rooms_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '1', 'callback_data': 'f_rooms-1'},
	{'text': '2', 'callback_data': 'f_rooms-2'},
	{'text': '3', 'callback_data': 'f_rooms-3'},
	 {'text': '4', 'callback_data': 'f_rooms-4'}],
	[{'text': lb.type_in[lang], 'callback_data': 'f_rooms_type-'},
	 {'text': lb.doesnt_matter[lang], 'callback_data': 'f_rooms-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_type_m-'}]
	]}
def f_rooms_type(lang='en'):
	return ll.f_rooms_type[lang]
###########################################################
def f_price_text(lang='en'):
	return ll.f_price_text[lang]
def f_price_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '300-500 €', 'callback_data': 'f_price-300/500'},
	{'text': '500-700 €', 'callback_data': 'f_price-500/700'}],
	[{'text': '700-1000 €', 'callback_data': 'f_price-700/1000'},
	{'text': f'{lb.more[lang]} 1000 €', 'callback_data': 'f_price->1000'}],
	[{'text': lb.type_in[lang], 'callback_data': 'f_price_type-'},
	 {'text': lb.doesnt_matter[lang], 'callback_data': 'f_price-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_view-'}]
	]}
def f_price_type(lang='en'):
	return ll.f_price_type[lang]
###########################################################
def f_city_text(lang='en'):
	return ll.f_city_text[lang]
###########################################################
def f_district_text(lang='en'):
	return ll.f_district_text[lang]
###########################################################
def f_route_type_text(lang='en'):
	return ll.f_route_type_text[lang]
def f_route_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.metro[lang], 'callback_data': 'f_routes_metro-'},
	 {'text': lb.bus[lang], 'callback_data': 'f_routes_bus-'}],
	[{'text': lb.trains[lang], 'callback_data': 'f_routes_trains-'}],
	[{'text': lb.back[lang], 'callback_data': 'f_loc_m-'}]
	]}
###########################################################
def f_routes_bus(lang='en'):
	return ll.f_routes_bus[lang]
###########################################################
def f_routes_train(lang='en'):
	return ll.f_routes_train[lang]
###########################################################
def f_routes_metro(lang='en'):
	return ll.f_routes_metro[lang]
###########################################################
def f_radius_text(lang='en'):
	return ll.f_radius_text[lang]
def f_radius_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': '300 m', 'callback_data': 'f_radius-0.3'},
	 {'text': '500 m', 'callback_data': 'f_radius-0.5'}],
	[{'text': '1 km', 'callback_data': 'f_radius-1'},
	 {'text': '2 km', 'callback_data': 'f_radius-2'}],
	[{'text': lb.back[lang], 'callback_data': 'f_loc_m-'}]
	]}
###########################################################
def f_sex_text(lang='en'):
	return ll.f_sex_text[lang]
def f_sex_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.male[lang], 'callback_data': 'f_sex-1'},
	 {'text': lb.female[lang], 'callback_data': 'f_sex-2'}],
	[{'text': lb.couple[lang], 'callback_data': 'f_sex-3'}],
	[{'text': lb.doesnt_matter[lang], 'callback_data': 'f_sex-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_pets_text(lang='en'):
	return ll.f_pets_text[lang]
def f_pets_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.yes[lang], 'callback_data': 'f_pets-1'},
	 {'text': lb.no[lang], 'callback_data': 'f_pets-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_smoke_text(lang='en'):
	return ll.f_smoke_text[lang]
def f_smoke_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.yes[lang], 'callback_data': 'f_smoke-1'},
	 {'text': lb.no[lang], 'callback_data': 'f_smoke-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_owner_text(lang='en'):
	return ll.f_owner_text[lang]
def f_owner_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.yes[lang], 'callback_data': 'f_owner-1'},
	 {'text': lb.no[lang], 'callback_data': 'f_owner-0'}],
	[{'text': lb.back[lang], 'callback_data': 'f_other_m-'}]
	]}
###########################################################
def f_name_text(lang='en'):
	return ll.f_name_text[lang]
def f_name_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.type_in[lang], 'callback_data': 'f_name_type-'}],
	[{'text': lb.leave_default[lang], 'callback_data': 'f_end-'}]
	]}
def f_name_type(lang='en'):
	return ll.f_name_type[lang]
###########################################################
def f_end_text(lang='en'):
	return ll.f_end_text[lang]

def direct_answer_err(lang='en'):
	return f'\n{ll.direct_answer_err[lang]} ({get_last_sec()})'
def geo_err(lang='en'):
	return f'\n{ll.direct_answer_err[lang]} ({get_last_sec()})'
def f_error_text(lang='en'):
	return ll.f_error_text[lang]
def back_menu_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.main_menu[lang], 'callback_data': 'main_menu-'}]
	]}

