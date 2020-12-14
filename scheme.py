
import backend.message_processing as mp
import backend.filter_composing as comp
import mockups.property_composing as p_comp
import mockups.funcs as p_funcs
import ui.funcs as funcs

from utils.utils import log_err


property_scheme = {
	'u_start': p_comp.add_property,
	'u_title': p_comp.title,
	'u_desc': p_comp.description,
	'u_contact': p_comp.contact_name,
	'u_phone': p_comp.contact_phone,
	'u_photo': p_comp.photo,
	'u_type': p_comp.type_,
	'u_rooms': p_comp.rooms,
	'u_district': p_comp.district,
	'u_price': p_comp.price,
	'u_sex': p_comp.sex,
	'u_pets': p_comp.pets,
	'u_smoke': p_comp.smoke,
	'u_owner': p_comp.owner
}



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
	'f_end_change': comp.change_filter,
	'f_error': comp.delete_filter
}

no_data_callbacks = [
	'f_start',
	'f_end',
	'f_end_change',
	'f_error',
	'f_rooms_type',
	'f_price_type',
	'f_name_type'
]

direct_answers = {
	'f_rooms_type': {'type_func': mp.rooms_to_int,
					'next_func': funcs.f_type_m},
	'f_price_type': {'type_func': mp.price_to_dict,
					 'next_func': funcs.f_view},
	'f_name_type': {'type_func': mp.name_to_str,
					'next_func': funcs.f_view},
	'u_title': {'type_func': mp.limit_string,
				'next_func': p_funcs.description},
	'u_desc': {'type_func': mp.limit_string,
			   'next_func': p_funcs.contact_name},
	'u_contact': {'type_func': mp.limit_string,
				  'next_func': p_funcs.contact_phone},
	'u_phone': {'type_func': mp.limit_string,
				'next_func': p_funcs.photo},
	'u_photo': {'type_func': mp.limit_string,
				'next_func': p_funcs.type_},

}

async_callbacks = {
	'user_filters': funcs.user_filters,
	'u_select': funcs.select_filter,
	'change_filter': funcs.change_user_filter,
	'del_filter': funcs.delete_user_filter,

	'u_start': p_funcs.title,
	'u_title': p_funcs.description,
	'u_desc': p_funcs.contact_name,
	'u_contact': p_funcs.contact_phone,
	'u_phone': p_funcs.photo,
	'u_photo': p_funcs.type_,
	'u_type': p_funcs.rooms,
	'u_rooms': p_funcs.district,
	'u_district': p_funcs.price,
	'u_price': p_funcs.sex,
	'u_sex': p_funcs.pets,
	'u_pets': p_funcs.smoke,
	'u_smoke': p_funcs.owner,
	'u_owner': p_funcs.owner
}

back_scheme = {

	# type
	'f_type': funcs.f_type_m,
	'f_rooms': funcs.f_type_m,

	# price to view
	'f_price': funcs.f_view,

	# loc
	'f_district': funcs.f_loc_m,
	'f_route': funcs.f_loc_m,
	'f_radius': funcs.f_loc_m,

	# other
	'f_sex': funcs.f_other_m,
	'f_pets': funcs.f_other_m,
	'f_smoke': funcs.f_other_m,
	'f_owner': funcs.f_other_m,

	'lang': funcs.main_menu
}

# each callback calls next menu
scheme = {
	'commands': {
		'/start': funcs.main_menu,
		'/select_lang': funcs.lang_select
	},
	'callbacks': {
		'select_lang': funcs.lang_select,
		'lang': funcs.main_menu,
		'f_view': funcs.f_view,
		'f_start': funcs.f_view,

		'f_loc_m': funcs.f_loc_m,
		'f_type_m': funcs.f_type_m,
		'f_other_m': funcs.f_other_m,

		'f_type': funcs.f_type,
		'f_rooms': funcs.f_rooms,
		'f_price': funcs.f_price,
		'f_district': funcs.f_district,

		'f_route_type': funcs.f_route_type,
		'f_routes_metro': funcs.f_routes_metro,
		'f_routes_bus': funcs.f_routes_bus,
		'f_radius': funcs.f_radius,
		
		
		'f_sex': funcs.f_sex,
		'f_pets': funcs.f_pets,
		'f_smoke': funcs.f_smoke,
		'f_owner': funcs.f_owner,
		'f_name_type': funcs.f_name_type,

		'f_end': funcs.main_menu,
		'f_end_change': funcs.main_menu,

		'f_rooms_type': funcs.f_rooms_type,
		'f_price_type': funcs.f_price_type,


		'main_menu': funcs.main_menu,
		'f_error': funcs.f_error
	}
}


async def async_process_callback(args, lang='en'):
	return await async_callbacks[args.callback](args, lang=lang)

def process_command(command, args, lang):
	if not lang:
		lang = 'en'
	return scheme['commands'][command](args, lang=lang)

def process_callback(callback, args=None, lang='en'):
	try:
		if args.callback_data:
			return back_scheme[callback](args, lang=lang)
		else:
			return scheme['callbacks'][callback](args, lang=lang)
	except Exception as err:
		# todo
		log_err(err)
		return scheme['callbacks']['f_error'](args, lang=lang)


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


