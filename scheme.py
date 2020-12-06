
import filters.message_processing as mp
import filters.compose as comp
import ui.funcs as funcs




filter_scheme = {
	'f_start': comp.add_filter,
	'f_type': comp.type_,
	'f_rooms': comp.rooms,
	'f_rooms_type': comp.rooms,
	'f_price': comp.price,
	'f_price_type': comp.price,
	'f_district': comp.district,
	'f_route': comp.route,
	'f_radius': comp.radius,
	'f_sex': comp.sex,
	'f_pets': comp.pets,
	'f_smoke': comp.smoke,
	'f_owner': comp.owner,
	'f_name_type': comp.name, # calls the end_filter also
	'f_end': comp.end_filter,
	'f_error': comp.delete_filter
}

callback_w_pages = [
	'f_price',
	'f_routes_metro',
	'f_routes_bus'
]

no_data_callbacks = [
	'f_start',
	'f_end',
	'f_error',
	'f_rooms_type',
	'f_price_type',
	'f_name_type'
]

direct_answers = {
	'f_rooms_type': {'type_func': mp.rooms_to_int,
					'next_func': funcs.f_price},
	'f_price_type': {'type_func': mp.price_to_dict,
					 'next_func': funcs.f_district},
	'f_name_type': {'type_func': mp.name_to_str,
					'next_func': funcs.f_end}
}

async_callbacks = {
	'user_filters': funcs.user_filters,
	'u_select': funcs.select_filter,
	'del_filter': funcs.delete_user_filter,
	'test': funcs.test
}

# args = bd, user_id, callback_data
callbacks_agrs_1 = [
	'u_select',
	'del_filter'
]

# each callback calls next menu
scheme = {
	'commands': {
		'/start': funcs.main_menu
	},
	'callbacks': {
		'f_start': funcs.f_type,
		'f_type': funcs.f_rooms,
		'f_rooms': funcs.f_price,
		'f_price': funcs.f_district,
		'f_district': funcs.f_route_type,

		'f_routes_metro': funcs.f_routes_metro,
		'f_routes_bus': funcs.f_routes_bus,
		'f_route': funcs.f_radius,
		'f_radius': funcs.f_sex,
		
		
		'f_sex': funcs.f_pets,
		'f_pets': funcs.f_smoke,
		'f_smoke': funcs.f_owner,
		'f_owner': funcs.f_name,
		'f_name': funcs.f_name,
		'f_name_type': funcs.f_name_type,

		'f_end': funcs.f_end,

		'f_rooms_type': funcs.f_rooms_type,
		'f_price_type': funcs.f_price_type,


		'main_menu': funcs.main_menu,
		'f_error': funcs.f_error
	}
}

async def async_process_callback(callback, *args):
	return await async_callbacks[callback](*args)

def process_command(command):
	return scheme['commands'][command]()

def process_callback(callback, *args):
	return scheme['callbacks'][callback](*args)

def process_answer(state, success=False):
	if success:
		return direct_answers[state]['next_func']
	else:
		return direct_answers[state]['type_func']

async def process_filter(callback, user_state, user_id, callback_data, from_direct_answer=False):
	try:
		if callback_data or callback in no_data_callbacks:
			if callback in filter_scheme:
				if not from_direct_answer and callback in direct_answers:
					return False
				func = filter_scheme[callback]
				await func(user_state, user_id, callback_data)
	except AssertionError as err:
		print(f'Assertion Error: {err}')
		return True


