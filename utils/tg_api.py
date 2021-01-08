import aiohttp
import ujson
from aiohttp import web

import config
from utils.utils import log_err
from utils.tg_exceptions import (read_exception,
								 BotBlocked)

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
	status, response = await _post_req(url, message, HEADERS, json_loads=True)
	if isinstance(response, BotBlocked):
		await response.process(chat_id)
		return status, None
	if response:
		response = response['result']['message_id']
	return status, response

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

async def send_invoice(chat_id, amount):
	url = API_URL+'sendInvoice'
	prices = [
		{
			'label': 'Dollars',
			'amount': 100
		}
	]
	message = {
		'chat_id': chat_id,
		'title': f'Donation {amount}',
		'description': 'description',
		'payload': 'test',
		'provider_token': config.PAY_TOKEN,
		'start_parameter': 'start',
		'currency': 'USD',
		'prices': prices
	}
	return (await _post_req(url, message, HEADERS))[0]

async def pre_checkout(update_id, pre_checkout_query_id):
	url = API_URL+'answerPreCheckoutQuery'
	answerPreCheckoutQuery = {
		'pre_checkout_query_id': pre_checkout_query_id,
		'ok': True,
		'error_message': 'error'
	}
	message = {
		'update_id': update_id,
		'pre_checkout_query': answerPreCheckoutQuery
	}
	return (await _post_req(url, answerPreCheckoutQuery, HEADERS))[0]

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
				message = await resp.read()
				log_err(err, message)
				exc = read_exception(message)
				if exc:
					return [web.Response(status=400), exc]
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
				message = await resp.read()
				log_err(err, message)
				return [web.Response(status=500), None]