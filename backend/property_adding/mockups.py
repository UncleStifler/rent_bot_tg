

import ui.lang_lines as ll
import ui.lang_buttons as lb

def start_property_text(lang='en'):
	return ll.ad_start[lang]
def start_property_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'main_menu-'},
	 {'text': lb.yes[lang], 'callback_data': 'u_start-'}]
	]}

# description

def u_title_text(lang='en'):
	return ll.ad_title[lang]
def u_title_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'main_menu-'}]
	]}

def u_description_text(lang='en'):
	return ll.ad_description[lang]
def u_description_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_start-'}]
	]}

def u_contact_text(lang='en'):
	return ll.ad_contact_name[lang]
def u_contact_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_title-'}]
	]}

def u_phone_text(lang='en'):
	return ll.ad_contact_phone[lang]
def u_phone_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_desc-'}]
	]}

def u_photo_text(lang='en'):
	return ll.ad_photo[lang]
def u_photo_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_contact-'}]
	]}

# to filter

def u_type_text(lang='en'):
	return ll.ad_type[lang]
def u_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.flat[lang], 'callback_data': 'u_type-0'},
	 {'text': lb.room[lang], 'callback_data': 'u_type-1'}],
	[{'text': lb.back[lang], 'callback_data': 'u_phone-'}]
	]}
###########################################################
def u_rooms_text(lang='en'):
	return ll.ad_rooms[lang]
def u_rooms_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_photo-'}]
	]}
###########################################################
def u_geo_text(lang='en'):
	return ll.ad_geo[lang]
def u_geo_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_type-'}]
	]}
###########################################################
def u_price_text(lang='en'):
	return ll.ad_price[lang]
def u_price_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_rooms-'}]
	]}
###########################################################
def u_sex_text(lang='en'):
	return ll.ad_sex[lang]
def u_sex_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.male[lang], 'callback_data': 'u_sex-1'},
	 {'text': lb.female[lang], 'callback_data': 'u_sex-2'}],
	[{'text': lb.both[lang], 'callback_data': 'u_sex-0'}],
	[{'text': lb.couple[lang], 'callback_data': 'u_sex-3'}],
	[{'text': lb.back[lang], 'callback_data': 'u_district-'}]
	]}
###########################################################
def u_pets_text(lang='en'):
	return ll.ad_pets[lang]
def u_pets_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.no[lang], 'callback_data': 'u_pets-0'},
	 {'text': lb.yes[lang], 'callback_data': 'u_pets-1'}],
	[{'text': lb.back[lang], 'callback_data': 'u_price-'}]
	]}
###########################################################
def u_smoke_text(lang='en'):
	return ll.ad_smoke[lang]
def u_smoke_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.no[lang], 'callback_data': 'u_smoke-0'},
	 {'text': lb.yes[lang], 'callback_data': 'u_smoke-1'}],
	[{'text': lb.back[lang], 'callback_data': 'u_sex-'}]
	]}
###########################################################
def u_owner_text(lang='en'):
	return ll.ad_owner[lang]
def u_owner_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.no[lang], 'callback_data': 'u_owner-0'},
	 {'text': lb.yes[lang], 'callback_data': 'u_owner-1'}],
	[{'text': lb.back[lang], 'callback_data': 'u_pets-'}]
	]}
###########################################################
def u_end_text(lang='en'):
	return ll.ad_end[lang]
def u_end_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': lb.back[lang], 'callback_data': 'u_smoke-'},
	 {'text': lb.next_[lang], 'callback_data': 'u_end-'}]
	]}
###########################################################


# def direct_answer_err(lang='en'):
# 	return l.direct_answer_err[lang]
# def f_error_text(lang='en'):
# 	return l.f_error_text[lang]

