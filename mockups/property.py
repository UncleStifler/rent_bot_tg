

# main menu
title = '''
Here you can add your own ad.
Start with typing ad title.
'''
###########################################################
type_text = '''
Choose the type of property you rent
'''
type_keyboard = {'inline_keyboard': [
	[{'text': 'Flat', 'callback_data': 'u_type-0'},
	 {'text': 'Room', 'callback_data': 'u_type-1'}]
	]}
###########################################################
district_text = '''
Choose the district where you rent
'''
###########################################################
contact_name_text = '''
Type in a name that will be shown in your ad
'''
###########################################################
contact_phone_text = '''
Type in a contact phone that will be shown in your ad
'''
###########################################################
owner_text = '''
Do you own the property you renting?
'''
owner_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_owner-1'},
	 {'text': 'No', 'callback_data': 'u_owner-0'}]
	]}
###########################################################
price_text = '''
Type in how much you ask for rent, in euros
'''
###########################################################
rooms_text = '''
How many rooms does your property have?
'''




###########################################################
sex_text = '''
Choose preferred tenant gender
'''
sex_keyboard = {'inline_keyboard': [
	[{'text': 'Male', 'callback_data': 'u_sex-1'},
	 {'text': 'Female', 'callback_data': 'u_sex-2'}],
	[{'text': 'Both', 'callback_data': 'u_sex-0'}]
	]}
###########################################################
smoke_text = '''
Do you allow the tenant to smoke?
'''
smoke_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_smoke-1'},
	 {'text': 'No', 'callback_data': 'u_smoke-0'}]
	]}
###########################################################
pets_text = '''
Do you allow pets in your property?
'''
pets_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'u_pets-1'},
	 {'text': 'No', 'callback_data': 'u_pets-0'}]
	]}
