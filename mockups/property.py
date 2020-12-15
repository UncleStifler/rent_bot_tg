

# description

def u_title_text(lang='en'):
	return 'Type in the title of your ad'
def u_title_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'main_menu-'}]
	]}

def u_description_text(lang='en'):
	return 'Type in the description of your ad'
def u_description_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_start-'}]
	]}

def u_contact_text(lang='en'):
	return 'Type in your name to contact you'
def u_contact_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_title-'}]
	]}

def u_phone_text(lang='en'):
	return 'Type in the phone number to contact you'
def u_phone_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_desc-'}]
	]}

def u_photo_text(lang='en'):
	return 'Send one good photo of your property'
def u_photo_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_contact-'}]
	]}

# to filter

def u_type_text(lang='en'):
	return 'Choose the type of property you rent'
def u_type_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Flat', 'callback_data': 'u_type-0'},
	 {'text': 'Room', 'callback_data': 'u_type-1'}],
	[{'text': 'Both', 'callback_data': 'u_type-2'}],
	[{'text': 'Back', 'callback_data': 'u_phone-'}]
	]}
###########################################################
def u_rooms_text(lang='en'):
	return 'Type in the number of rooms your property have'
def u_rooms_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_photo-'}]
	]}
###########################################################
def u_district_text(lang='en'):
	return 'Choose the district where is your property located'
# back - u_type
###########################################################
def u_price_text(lang='en'):
	return 'Type in the price'
def u_price_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Back', 'callback_data': 'u_rooms-'}]
	]}
###########################################################
def u_sex_text(lang='en'):
	return 'To what gender do you rent?'
def u_sex_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'Male', 'callback_data': 'u_sex-1'},
	 {'text': 'Female', 'callback_data': 'u_sex-2'}],
	[{'text': 'Both', 'callback_data': 'u_sex-0'}],
	[{'text': 'Back', 'callback_data': 'u_district-'}]
	]}
###########################################################
def u_pets_text(lang='en'):
	return 'Do you allow pets?'
def u_pets_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'No', 'callback_data': 'u_pets-0'},
	 {'text': 'Yes', 'callback_data': 'u_pets-1'}],
	[{'text': 'Back', 'callback_data': 'u_price-'}]
	]}
###########################################################
def u_smoke_text(lang='en'):
	return 'Do you allow smoke?'
def u_smoke_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'No', 'callback_data': 'u_smoke-0'},
	 {'text': 'Yes', 'callback_data': 'u_smoke-1'}],
	[{'text': 'Back', 'callback_data': 'u_sex-'}]
	]}
###########################################################
def u_owner_text(lang='en'):
	return 'Do you own the property you rent?'
def u_owner_keyboard(lang='en'):
	return {'inline_keyboard': [
	[{'text': 'No', 'callback_data': 'u_owner-0'},
	 {'text': 'Yes', 'callback_data': 'u_owner-1'}],
	[{'text': 'Back', 'callback_data': 'u_pets-'}]
	]}
###########################################################

# def direct_answer_err(lang='en'):
# 	return l.direct_answer_err[lang]
# def f_error_text(lang='en'):
# 	return l.f_error_text[lang]

