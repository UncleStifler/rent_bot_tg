
import backend.message_processing as mp
import backend.filter_adding.filter_composing as f_comp
import backend.property_adding.property_composing as p_comp
import backend.property_adding.funcs as p_funcs
import backend.filter_adding.funcs as f_funcs
import backend.general.funcs as funcs
import backend.admin.funcs as adm

from utils.utils import log_err




filter_scheme = {
	'f_start': f_comp.add_filter,
	'f_type': f_comp.type_,
	'f_rooms': f_comp.rooms,
	'f_rooms_type': f_comp.rooms,
	'f_price': f_comp.price,
	'f_price_type': f_comp.price,
	'f_city': f_comp.city,
	'f_district': f_comp.district,
	'f_route': f_comp.route,
	'f_radius': f_comp.radius,
	'f_sex': f_comp.sex,
	'f_pets': f_comp.pets,
	'f_smoke': f_comp.smoke,
	'f_owner': f_comp.owner,
	'f_name_type': f_comp.name,
	'f_end': f_comp.end_filter,
	'f_end_change': f_comp.change_filter,
	'f_error': f_comp.delete_filter,


	'u_start': p_comp.add_property,
	'u_title': p_comp.title,
	'u_desc': p_comp.description,
	'u_contact': p_comp.contact_name,
	'u_phone': p_comp.contact_phone,
	'u_photo': p_comp.photo,
	'u_type': p_comp.type_,
	'u_rooms': p_comp.rooms,
	'u_geo': p_comp.geo,
	'u_price': p_comp.price,
	'u_sex': p_comp.sex,
	'u_pets': p_comp.pets,
	'u_smoke': p_comp.smoke,
	'u_owner': p_comp.owner,
	'u_end': p_comp.send_property
}

no_data_callbacks = [
	'f_start',
	'f_end',
	'f_end_change',
	'f_error',
	'f_rooms_type',
	'f_price_type',
	'f_name_type',
	'u_start_page',
	'u_start',
	'u_end'
]

direct_answers = {
	'f_rooms_type': {'type_func': mp.to_int,
					'next_func': f_funcs.f_type_m,
					 'core_func': f_funcs.f_rooms_type},
	'f_price_type': {'type_func': mp.price_to_dict,
					 'next_func': f_funcs.f_view,
					 'core_func': f_funcs.f_price_type},
	'f_name_type': {'type_func': mp.limit_string_100,
					'next_func': f_funcs.f_view,
					'core_func': f_funcs.f_name_type},
	'u_title': {'type_func': mp.limit_string,
				'next_func': p_funcs.description,
				'core_func': p_funcs.title},
	'u_desc': {'type_func': mp.limit_string_2000,
			   'next_func': p_funcs.contact_name,
			   'core_func': p_funcs.description},
	'u_contact': {'type_func': mp.limit_string,
				  'next_func': p_funcs.contact_phone,
				  'core_func': p_funcs.contact_name},
	'u_phone': {'type_func': mp.limit_string,
				'next_func': p_funcs.photo,
				'core_func': p_funcs.contact_phone},
	'u_photo': {'type_func': mp.photo_check,
				'next_func': p_funcs.type_,
				'core_func': p_funcs.photo},
	'u_rooms': {'type_func': mp.to_int,
				'next_func': p_funcs.geo,
				'core_func': p_funcs.rooms},
	'u_geo': {'type_func': mp.valid_geo,
			  'next_func': p_funcs.price,
			  'core_func': p_funcs.geo},
	'u_price': {'type_func': mp.price_to_int,
				'next_func': p_funcs.sex,
				'core_func': p_funcs.price},
	'a_auth': {'type_func': mp.auth_,
				'next_func': adm.admin,
				'core_func': adm.admin_auth},
	'a_mailing': {'type_func': adm.mailing_,
				  'next_func': adm.admin_mailing_step2,
				  'core_func': adm.admin_mailing
	},
}

back_scheme = {

	# type
	'f_type': f_funcs.f_type_m,
	'f_rooms': f_funcs.f_type_m,

	# price to view
	'f_price': f_funcs.f_view,

	# loc
	'f_city': f_funcs.f_loc_m,
	'f_district': f_funcs.f_loc_m,
	'f_route': f_funcs.f_loc_m,
	'f_radius': f_funcs.f_loc_m,

	# other
	'f_sex': f_funcs.f_other_m,
	'f_pets': f_funcs.f_other_m,
	'f_smoke': f_funcs.f_other_m,
	'f_owner': f_funcs.f_other_m,

	'lang': funcs.main_menu
}

scheme = {
	'commands': {
		'/start': funcs.main_menu,
		'/select_lang': funcs.lang_select,
		'/admin': adm.admin_auth,
		'/donation_end': funcs.donation_end
	},
	'callbacks': {
		'select_lang': funcs.lang_select,
		'lang': funcs.main_menu,
		'donation_menu': funcs.donation,
		'f_view': f_funcs.f_view,
		'f_start': f_funcs.f_view,

		'f_loc_m': f_funcs.f_loc_m,
		'f_type_m': f_funcs.f_type_m,
		'f_other_m': f_funcs.f_other_m,

		'f_type': f_funcs.f_type,
		'f_rooms': f_funcs.f_rooms,
		'f_price': f_funcs.f_price,
		'f_city': f_funcs.f_city,
		'f_district': f_funcs.f_district,

		'f_route_type': f_funcs.f_route_type,
		'f_routes_metro': f_funcs.f_routes_metro,
		'f_routes_bus': f_funcs.f_routes_bus,
		'f_routes_trains': f_funcs.f_routes_trains,
		'f_radius': f_funcs.f_radius,
		
		
		'f_sex': f_funcs.f_sex,
		'f_pets': f_funcs.f_pets,
		'f_smoke': f_funcs.f_smoke,
		'f_owner': f_funcs.f_owner,
		'f_end': funcs.main_menu,
		'f_end_change': funcs.main_menu,


		'main_menu': funcs.main_menu,
		'f_error': funcs.f_error,


		'user_filters': f_funcs.user_filters,
		'u_select': f_funcs.select_filter,
		'change_filter': f_funcs.change_user_filter,
		'del_filter': f_funcs.delete_user_filter,

		'f_name_type': f_funcs.f_name_type,
		'f_rooms_type': f_funcs.f_rooms_type,
		'f_price_type': f_funcs.f_price_type,

		'u_start_page': p_funcs.start_page,
		'u_start': p_funcs.title,
		'u_title': p_funcs.description,
		'u_desc': p_funcs.contact_name,
		'u_contact': p_funcs.contact_phone,
		'u_phone': p_funcs.photo,
		'u_photo': p_funcs.type_,
		'u_type': p_funcs.rooms,
		'u_rooms': p_funcs.geo,
		'u_geo': p_funcs.price,
		# 'u_city': p_funcs.district,
		# 'u_district': p_funcs.price,
		'u_price': p_funcs.sex,
		'u_sex': p_funcs.pets,
		'u_pets': p_funcs.smoke,
		'u_smoke': p_funcs.owner,
		'u_owner': p_funcs.end,
		'u_end': funcs.main_menu,

		'a_main': adm.admin,
		'a_main_from_ad': adm.admin,
		'a_show': adm.show_last_ad,
		'a_decline': adm.decline_ad,
		'a_accept': adm.accept_ad,
		'a_stats': adm.admin_statistics,
		'a_mailing': adm.admin_mailing,
		'a_mailing_step3': adm.admin_mailing_step3,
		'a_mailing_rus': adm.admin_mailing_step4_ru,
		'a_mailing_en': adm.admin_mailing_step4_en,
		'a_mailing_es': adm.admin_mailing_step4_es,
		'a_mailing_publish': adm.admin_post_publish
	}
}


async def process_command(command, args, lang):
	if not lang:
		lang = 'en'
	return await scheme['commands'][command](args, lang=lang)

async def process_callback(callback, args=None, lang='en'):
	try:
		if args.callback_data and callback in back_scheme:
			return await back_scheme[callback](args, lang=lang)
		else:
			return await scheme['callbacks'][callback](args, lang=lang)
	except Exception as err:
		# todo
		log_err(err)
		return await scheme['callbacks']['f_error'](args, lang=lang)


def process_answer(state, success=False, error=False):
	if error:
		return direct_answers[state]['core_func']
	if success:
		return direct_answers[state]['next_func']
	else:
		return direct_answers[state]['type_func']

async def process_filter(callback, user_state, user_id, callback_data, from_direct_answer=False):
	try:
		if callback_data or callback in no_data_callbacks:
			if callback in filter_scheme:
				if not from_direct_answer and callback in direct_answers and callback not in ['u_photo']:
					return False
				await filter_scheme[callback](user_state, user_id, callback_data)
	except AssertionError as err:
		print(f'Assertion Error: {err}')
		return True


