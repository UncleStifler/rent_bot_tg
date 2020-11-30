
import scheme

def get_args(bd,
             pool,
             user_id,
             callback,
             callback_data,
             page):
    if page is not None:
        args = [bd, page]
    elif callback in scheme.callbacks_agrs_1:
        args = [bd, user_id, callback_data, pool]
    elif callback in scheme.async_callbacks:
        args = [user_id, pool]
    else:
        args = []
    return args


def get_callback(data, bd, pool):
    user_id = data['callback_query']['message']['chat']['id']
    callback, callback_data = data['callback_query']['data'].split('-')
    if any(callback.startswith(x) for x in scheme.callback_w_pages):
        try:
            splited_callback = callback.split('/')
            callback = splited_callback[0]
            page = int(splited_callback[1])
        except IndexError:
            page = 0
    else:
        page = None
    args = get_args(bd, pool, user_id, callback, callback_data, page)
    return user_id, callback, callback_data, args

def get_message(data):
    user_id = data['message']['chat']['id']
    message = data['message']['text']
    message_id = data['message']['message_id']
    return user_id, message, message_id