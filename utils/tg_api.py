import aiohttp
import ujson
from aiohttp import web

import config
from utils.utils import log_err

API_URL = f'https://api.telegram.org/bot{config.TOKEN}/'
HEADERS = {'Content-Type': 'application/json'}

def _get_message_for_sent(chat_id,
						  text,
						  keyboard,
						  update,
						  markdown=True):
	message = {
		'chat_id': chat_id,
		'text': text
	}
	if keyboard:
		message.update({'reply_markup': keyboard})
	if update:
		message.update({'message_id': update})
	if markdown:
		message.update({'parse_mode': 'markdown'})
		message.update({'disable_web_page_preview': False})
	return message

def _get_message_for_delete(chat_id, message_id):
	return {
		'chat_id': chat_id,
		'message_id': message_id
	}

async def send_message(chat_id, text, keyboard=None, update=None):
	message = _get_message_for_sent(chat_id, text, keyboard, update)
	url = API_URL+'sendMessage'
	if update:
		url = API_URL+'editMessageText'
	async with aiohttp.ClientSession() as session:
		async with session.post(url,
								data=ujson.dumps(message),
								headers=HEADERS) as resp:
			try:
				assert resp.status == 200 or resp.status == 400
				if resp.status == 400:
					print(message)
				response = await resp.text()
				id_ = ujson.loads(response)['result']['message_id']
				return [web.Response(status=200), id_]
			except Exception as err:
				log_err(err)
				print(await resp.text())
				return [web.Response(status=500), None]

async def delete_message(chat_id, message_id):
	message = _get_message_for_delete(chat_id, message_id)
	url = API_URL+'deleteMessage'
	return (await _post_req(url, message, HEADERS))[0]

async def send_location(chat_id, lat_lon):
	lat, lon = lat_lon.split('|')
	url = API_URL+'sendLocation'
	message = {
		'chat_id': chat_id,
		'latitude': float(lat),
		'longitude': float(lon)
	}
	return (await _post_req(url, message, HEADERS))[0]

async def get_file_path(file_id):
	url = f'{API_URL}getFile?file_id={file_id}'
	return (await _post_req(url, None, HEADERS, json_loads=True))[1]

async def download_file(file_path):
	url = f'https://api.telegram.org/file/bot{config.TOKEN}/{file_path}'
	return (await _get_req(url, HEADERS))[1]


async def _post_req(url, data, headers, json_loads=False):
	async with aiohttp.ClientSession() as session:
		async with session.post(url,
								data=ujson.dumps(data),
								headers=headers) as resp:
			try:
				assert resp.status == 200
				response = await resp.read()
				if json_loads:
					response = ujson.loads(response)
				return [web.Response(status=200), response]
			except Exception as err:
				log_err(err)
				print(await resp.text())
				return [web.Response(status=500), None]

async def _get_req(url, headers, json_loads=False):
	async with aiohttp.ClientSession() as session:
		async with session.get(url,
							   headers=headers) as resp:
			try:
				assert resp.status == 200
				response = await resp.read()
				if json_loads:
					response = ujson.loads(response)
				return [web.Response(status=200), response]
			except Exception as err:
				log_err(err)
				print(await resp.text())
				return [web.Response(status=500), None]