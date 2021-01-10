import asyncio
import ssl
from aiohttp import web
from loguru import logger

import config
import scheme
import db.asql as asql
from googletrans.client import Translator
from utils.tg_api import send_message, delete_message
from backend.photos import process_file
from backend.user_state import UserState
from backend.data_updater import DataUpdater
from backend.callbacks_processing import get_callback
from backend.callbacks_processing import get_args
from backend.callbacks_processing import get_message
from backend.callbacks_processing import read_request
from backend.items_sending import process_from_filter_app
from utils.filters_api import send_show_more
from utils.tg_api import (send_location,
                          send_invoice,
                          pre_checkout)
from utils.utils import log_err


logger.add('app.log', format='{time} {level} {message}', level='DEBUG',
	enqueue=True)

async def process_answer(user_id, message, pool, lang='en'):
    state = user_state.get_state(user_id)
    prev_message_id = await user_state.get_message_id(user_id)
    args = get_args(user_state, db_data, pool, user_id)
    try:
        if state == 'u_geo':
            data = await scheme.process_answer(state)(message, args)
        else:
            data = scheme.process_answer(state)(message)
        assert data
        await user_state.change_state(user_id, None)
        filter_process_error = await scheme.process_filter(state,
                                                           user_state,
                                                           user_id,
                                                           data,
                                                           from_direct_answer=True)

        if filter_process_error:
            text, keyboard = await scheme.process_callback('f_error',
                                                     args,
                                                     lang=lang)
        else:
            text, keyboard = await scheme.process_answer(state,
                                                   success=True)(args,
                                                                 lang=lang)

        response, message_id = await send_message(user_id,
                                                  text,
                                                  keyboard,
                                                  prev_message_id)
        return response

    except AssertionError:
        args.error = True
        text, keyboard = await scheme.process_answer(state,
                                                     error=True)(args,
                                                                 lang=lang)
        response, message_id = await send_message(user_id,
                                                  text,
                                                  keyboard,
                                                  prev_message_id)
        return response

async def delete_bot_message(user_id):
    prev_message_id = await user_state.get_message_id(user_id)
    if prev_message_id:
        await delete_message(user_id, prev_message_id)
        await user_state.change_message_id(user_id, None)

async def tg_handler(request):
    pool, data = await read_request(request)
    print(data)
    try:
        if 'pre_checkout_query' in data:
            update_id = data['update_id']
            pre_checkout_id = data['pre_checkout_query']['id']
            await pre_checkout(update_id, pre_checkout_id)
            return web.Response(status=200)

        if 'callback_query' in data:
            user_id, callback, callback_data, args = get_callback(data,
                                                                  user_state,
                                                                  db_data,
                                                                  pool)
            lang = await user_state.get_lang(args.user_id)
            print(f'{callback = }')
            print(callback_data)

            if callback == 'donation':
                await send_invoice(user_id, callback_data, lang)
                return web.Response(status=200)

            if callback == 'show_more':
                await send_show_more(callback_data)
                await delete_bot_message(user_id)
                return web.Response(status=200)

            if callback == 'map':
                await send_location(user_id, callback_data)
                await delete_bot_message(user_id)
                return web.Response(status=200)

            if callback == 'lang':
                lang = callback_data
                await user_state.change_lang(args.user_id, lang)

            filter_process_error = await scheme.process_filter(callback,
                                                               user_state,
                                                               user_id,
                                                               callback_data)
            if filter_process_error:
                text, keyboard = await scheme.process_callback('f_error',
                                                               lang=lang)
            else:
                text, keyboard = await scheme.process_callback(args.callback,
                                                               args,
                                                               lang=lang)

            if callback in ['f_end_change', 'f_end']:
                await delete_bot_message(user_id)
                return web.Response(status=200)

            prev_message_id = await user_state.get_message_id(user_id)
            response, message_id = await send_message(user_id,
                                                      text,
                                                      keyboard,
                                                      prev_message_id)

            await user_state.change_message_id(user_id, message_id)
            return response

        elif 'message' in data:
            user_id, message, message_id, file_id, location, payment = get_message(data)
            args = get_args(user_state, db_data, pool, user_id)
            lang = await user_state.get_lang(user_id)
            # print(f'{message = }')

            await delete_message(user_id, message_id)

            if payment:
                message = '/donation_end'

            if location:
                message = location

            if file_id:
                if user_state.get_state(user_id) == 'u_photo':
                    message = await process_file(file_id)

            if not message:
                return web.Response(status=200)

            if not lang:
                message = '/select_lang'

            try:
                if isinstance(message, dict):
                    raise KeyError

                text, keyboard = await scheme.process_command(message,
                                                              args,
                                                              lang)


                response, message_id = await send_message(user_id,
                                                          text,
                                                          keyboard)
                await user_state.change_message_id(user_id, message_id)
                return response
            except KeyError:
                if user_state.get_state(user_id):
                    return await process_answer(user_id, message, pool, lang=lang)

    except Exception as err:
        log_err(err)
    finally:
        if config.branch == 'dev':
            print(user_state.state)
            print(user_state.filters)
        return web.Response(status=200)

async def send_results_handler(request):
    pool, data = await read_request(request)
    await process_from_filter_app(data, pool, db_data, user_state, translator)
    return web.Response(status=200)

async def init_app():
    app = web.Application()
    app['pool'] = await asql.get_pool()
    app.router.add_post('/rent_bot/', tg_handler)
    app.router.add_post('/send_results/', send_results_handler)
    return app

@logger.catch
def main():
    loop = asyncio.get_event_loop()
    try:
        app = loop.run_until_complete(init_app())
        global db_data
        db_data = DataUpdater(app['pool'])
        global user_state
        user_state = UserState(app['pool'])
        global translator
        translator = Translator(service_urls=[
            'translate.google.com'
        ])


        if config.branch == 'dev':
            web.run_app(app,
                        host=config.WEBHOOK_LISTEN,
                        port=config.WEBHOOK_PORT)
        else:
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.load_cert_chain(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRIV)
            web.run_app(app,
                        host=config.WEBHOOK_LISTEN,
                        port=config.WEBHOOK_PORT,
                        ssl_context=context)
    except Exception as e:
        print(f'Error create server: {e}')
    finally:
        pass
    loop.close()


if __name__ == '__main__':
    main()

