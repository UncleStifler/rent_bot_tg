
# second test commit

main_menu_text = {'en': 'Welcome. This is start page.',
				  'es': 'Bienvenido. Esta es la página de inicio.'}

x = lambda y: y*2

print(x(4))

z = {24: {24, x(5)}}
print(z)



x = {'inline_keyboard': [
	[{'text': 'Add filter', 'callback_data': 'f_start-'}],
	[{'text': 'My filters', 'callback_data': 'user_filters-'}]
	]}