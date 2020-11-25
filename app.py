import asyncio
import ujson

##
import traceback

from aiohttp import web
from loguru import logger

import config
import scheme

from utils.tg_api import send_message, delete_message
from utils.user_state import UserState
from db.data_updater import DataUpdater
from ui.utils import get_callback
from ui.utils import get_message





logger.add('app.log', format='{time} {level} {message}', level='DEBUG',
	enqueue=True)

# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.load_cert_chain(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRIV)




async def process_answer(user_id, message):
    state = user_state.get_state(user_id)
    try:
        data = scheme.process_answer(state)(message)
        assert data
        user_state.change_state(user_id, None)
        filter_process_error = await scheme.process_filter(state,
                                                     user_state,
                                                     user_id,
                                                     data,
                                                     from_direct_answer=True)

        if filter_process_error:
            text, keyboard = scheme.process_callback('f_error')()
        else:
            text, keyboard = scheme.process_answer(state,
                                               success=True)()

        response, message_id = await send_message(user_id,
                                                  text,
                                                  keyboard,
                                                  user_state.get_message_id(user_id))
        return response

    except AssertionError:
        text, keyboard = scheme.process_callback(state)(err=True)
        response, message_id = await send_message(user_id,
                                                  text,
                                                  keyboard,
                                                  user_state.get_message_id(user_id))
        return response


async def handler(request):
    data = await request.read()
    data = ujson.loads(data)
    # print(data)
    try:
        if 'callback_query' in data:
            user_id, callback, callback_data, page = get_callback(data)
            print(f'{callback = }')
            args = [bd_data, page] if page is not None else []

            filter_process_error = await scheme.process_filter(callback,
                                                         user_state,
                                                         user_id,
                                                         callback_data)
            if filter_process_error:
                text, keyboard = scheme.process_callback('f_error')()
            else:
                text, keyboard = scheme.process_callback(callback)(*args)
                if callback in scheme.direct_answers:
                    user_state.change_state(user_id, callback)

            response, message_id = await send_message(user_id,
                                                      text,
                                                      keyboard,
                                                      user_state.get_message_id(user_id))

            user_state.change_message_id(user_id, message_id)
            return response

        elif 'message' in data:
            user_id, message, message_id = get_message(data)
            print(f'{message = }')

            await delete_message(user_id, message_id)

            if user_state.get_state(user_id):
                return await process_answer(user_id, message)

            if message in scheme.scheme['commands']:
                text, keyboard = scheme.process_command(message)()

                response, message_id = await send_message(user_id,
                                                          text,
                                                          keyboard)
                user_state.change_message_id(user_id, message_id)
                return response

    except Exception as err:
        tb = '\n'.join(traceback.format_tb(err.__traceback__))
        logger.error(f'\n{err}\n{tb}')
    finally:

        print(user_state.state)
        print(user_state.filters)
        return web.Response(status=200)


async def init_app():
    app = web.Application()
    app.router.add_post('/rent_bot/', handler)
    return app

@logger.catch
def main():
    loop = asyncio.get_event_loop()
    try:
        global user_state
        user_state = UserState()
        global bd_data
        bd_data = DataUpdater()

        app = loop.run_until_complete(init_app())
        web.run_app(app,
                    host=config.WEBHOOK_LISTEN,
                    port=config.WEBHOOK_PORT)

        # todo before deploy change ssl
        # web.run_app(app,
        #             host=config.WEBHOOK_LISTEN,
        #             port=config.WEBHOOK_PORT,
        #             ssl_context=context)
    except Exception as e:
        print(f'Error create server: {e}')
    finally:
        pass
    loop.close()


if __name__ == '__main__':
    main()

