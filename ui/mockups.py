

# type of callback data
# callback-data


# main menu
main_menu_text = '''
Welcome. This is start page.
'''
main_menu_keyboard = {'inline_keyboard': [
	[{'text': 'Add filter', 'callback_data': 'f_start-'}]
	]}




###########################################################
f_type_text = '''
Choose the type of property you are looking for
'''
f_type_keyboard = {'inline_keyboard': [
	[{'text': 'Flat', 'callback_data': 'f_type-0'},
	 {'text': 'Room', 'callback_data': 'f_type-1'}]
	]}
###########################################################
f_rooms_text = '''
How many rooms are you looking for?
'''
f_rooms_keyboard = {'inline_keyboard': [
	[{'text': '1', 'callback_data': 'f_rooms-1'},
	{'text': '2', 'callback_data': 'f_rooms-2'},
	{'text': '3', 'callback_data': 'f_rooms-3'},
	 {'text': '4', 'callback_data': 'f_rooms-4'}],
	[{'text': 'Type in', 'callback_data': 'f_rooms_type-'},
	 {'text': "Doesn't matter", 'callback_data': 'f_rooms-0'}]
	]}
f_rooms_type = '''
Type in number of rooms
Example: 3
'''
###########################################################
f_price_text = '''
You can choose a price range from below or enter your own. You can also skip this step.
'''
f_price_keyboard = {'inline_keyboard': [
	[{'text': '300-500', 'callback_data': 'f_price-300/500'},
	{'text': '500-700', 'callback_data': 'f_price-500/700'}],
	[{'text': '700-1000', 'callback_data': 'f_price-700/1000'},
	{'text': '> 1000', 'callback_data': 'f_price->1000'}],
	[{'text': 'Type in', 'callback_data': 'f_price_type-'},
	 {'text': "Doesn't matter", 'callback_data': 'f_price-0'}]
	]}
f_price_type = '''
Type in your price range
Example: 500-1000, >500, <500
'''
###########################################################
f_district_text = '''
Select the district where the property is located
'''
###########################################################
f_route_type_text = '''
Our algorithm can select for you properties located near public transport routes. What kind of transport do you need?
'''
f_route_type_keyboard = {'inline_keyboard': [
	[{'text': 'Metro', 'callback_data': 'f_routes_metro-'},
	 {'text': 'Bus', 'callback_data': 'f_routes_bus-'}],
	[{'text': 'Skip', 'callback_data': 'f_radius-'}]
	]}
###########################################################
f_routes_bus = '''
Please select the bus route you need.
'''
###########################################################
f_routes_metro = '''
Please select the metro line you need.
'''
###########################################################
f_radius_text = '''
Choose the maximum distance to the stop.
'''
f_radius_keyboard = {'inline_keyboard': [
	[{'text': '300 m', 'callback_data': 'f_radius-0.3'},
	 {'text': '500 m', 'callback_data': 'f_radius-0.5'}],
	[{'text': '1 km', 'callback_data': 'f_radius-1'},
	 {'text': '2 km', 'callback_data': 'f_radius-2'}]
	]}
###########################################################
f_sex_text = '''
Choose the gender your landlord prefers
(it doesn't matter if you looking for a flat)
'''
f_sex_keyboard = {'inline_keyboard': [
	[{'text': 'Male', 'callback_data': 'f_sex-1'},
	 {'text': 'Female', 'callback_data': 'f_sex-2'}],
	[{'text': "Doesn't matter", 'callback_data': 'f_sex-0'}],
	[{'text': 'Finish adding filter', 'callback_data': 'f_name-'}]
	]}
###########################################################
f_pets_text = '''
Is it important to you that the landlord allowed pets?
(it doesn't matter if you looking for a flat)
'''
f_pets_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'f_pets-1'},
	 {'text': 'No', 'callback_data': 'f_pets-0'}],
	[{'text': 'Finish adding filter', 'callback_data': 'f_name-'}]
	]}
###########################################################
f_smoke_text = '''
Is it important to you that the landlord allowed smoking?
(it doesn't matter if you looking for a flat)
'''
f_smoke_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'f_smoke-1'},
	 {'text': 'No', 'callback_data': 'f_smoke-0'}],
	[{'text': 'Finish adding filter', 'callback_data': 'f_name-'}]
	]}
###########################################################
f_owner_text = '''
Is it important for you that the landlord owns the property?
'''
f_owner_keyboard = {'inline_keyboard': [
	[{'text': 'Yes', 'callback_data': 'f_owner-1'},
	 {'text': 'No', 'callback_data': 'f_owner-0'}],
	[{'text': 'Finish adding filter', 'callback_data': 'f_name-'}]
	]}
###########################################################
f_name_text = '''
In case you have many filters, please enter a filter name to differentiate between results.
Otherwise, the name will be default ('Filter').
'''
f_name_keyboard = {'inline_keyboard': [
	[{'text': 'Type in', 'callback_data': 'f_name_type-'}],
	[{'text': 'Leave default', 'callback_data': 'f_end-'}]
	]}
f_name_type = '''
The filter name must be in english letters and less than 100 in length.
Example: Only rooms with price less than 1000 euro.
'''
###########################################################
f_end_text = '''
The filter was added successfully
'''
f_end_keyboard = {'inline_keyboard': [
	[{'text': 'Main Menu', 'callback_data': 'main_menu-'}]
	]}




direct_answer_err = '''
\nSorry, I can't read this. Please, follow the example above
'''
f_error_text = '''
Sorry, something went wrong with filter adding. Try again or contact us.
'''
f_error_keyboard = {'inline_keyboard': [
	[{'text': 'Main Menu', 'callback_data': 'main_menu-'}],
	[{'text': 'Contact developers', 'callback_data': 'main_menu-'}]
	]}
