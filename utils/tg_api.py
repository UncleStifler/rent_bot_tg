import aiohttp
import ujson
from aiohttp import web

import config

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
				response = await resp.text()
				id_ = ujson.loads(response)['result']['message_id']
				return [web.Response(status=200), id_]
			except Exception as err:
				print(err)
				print(await resp.text())
				return [web.Response(status=500), None]



async def delete_message(chat_id, message_id):
	message = _get_message_for_delete(chat_id, message_id)
	url = API_URL+'deleteMessage'
	async with aiohttp.ClientSession() as session:
		async with session.post(url,
								data=ujson.dumps(message),
								headers=HEADERS) as resp:
			try:
				assert resp.status == 200
			except AssertionError:
				return web.Response(status=500)
	return web.Response(status=200)