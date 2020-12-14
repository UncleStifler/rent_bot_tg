

# description

def u_title_text(lang='en'):
	return 'Type in the title of your ad'

def u_description_text(lang='en'):
	return 'Type in the description of your ad'

def u_contact_text(lang='en'):
	return 'Type in your name to contact you'

def u_phone_text(lang='en'):
	return 'Type in the phone number to contact you'

def u_photo_text(lang='en'):
	return 'Send one good photo of your property'

# to filter

def u_type_text(lang='en'):
	return 'Choose the type of property you rent'
def u_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Flat', 'callback_data': 'u_type-0'},
	 {'text': 'Room', 'callback_data': 'u_type-1'}]
	]}
###########################################################
def u_rooms_text(lang='en'):
	return 'Type in the number of rooms your property have'
def u_rooms_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def u_district_text(lang='en'):
	return 'Choose the district where is your property located'
###########################################################
def u_price_text(lang='en'):
	return 'Type in the price'
def u_price_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def u_sex_text(lang='en'):
	return 'To what gender do you rent?'
def u_sex_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Male', 'callback_data': 'u_type-0'},
	 {'text': 'Female', 'callback_data': 'u_type-1'}],
	[{'text': 'Both', 'callback_data': 'f_type_m-'}],
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def u_pets_text(lang='en'):
	return 'Do you allow pets?'
def u_pets_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_type-0'},
	 {'text': 'No', 'callback_data': 'u_type-1'}],
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def u_smoke_text(lang='en'):
	return 'Do you allow smoke?'
def u_smoke_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_type-0'},
	 {'text': 'No', 'callback_data': 'u_type-1'}],
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################
def u_owner_text(lang='en'):
	return 'Do you own the property you rent?'
def u_owner_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_type-0'},
	 {'text': 'No', 'callback_data': 'u_type-1'}],
	[{'text': 'Back', 'callback_data': 'f_type_m-'}]
	]}
###########################################################

# def direct_answer_err(lang='en'):
# 	return l.direct_answer_err[lang]
# def f_error_text(lang='en'):
# 	return l.f_error_text[lang]

