
import ujson

import scheme

async def read_request(request):
    pool = request.app['pool']
    data = await request.read()
    data = ujson.loads(data)
    return pool, data


class _DataArgs:
    def __init__(self,
                 pool,
                 state,
                 db,
                 user_id,
                 callback=None,
                 callback_data=None,
                 page=None):
        self.pool = pool
        self.state = state
        self.db = db
        self.user_id = user_id
        self.callback = callback
        self.callback_data = callback_data
        self.page = page
        self.error = False


# def get_message(data, db, pool, state):
#

def get_args(state, db, pool, user_id):
    return _DataArgs(pool,
                     state,
                     db,
                     user_id)


def get_callback(data, state, db, pool):
    user_id = data['callback_query']['message']['chat']['id']
    callback, callback_data = data['callback_query']['data'].split('-')
    try:
        splited_callback = callback.split('/')
        callback = splited_callback[0]
        page = int(splited_callback[1])
    except IndexError:
        page = None
    args = _DataArgs(pool,
                     state,
                     db,
                     user_id,
                     callback,
                     callback_data,
                     page)
    return user_id, callback, callback_data, args

def get_message(data):
    user_id = data['message']['chat']['id']
    message_id = data['message']['message_id']
    if 'location' in data['message']:
        location = data['message']['location']
    else:
        location = None
    if 'photo' in data['message']:
        file_id = data['message']['photo'][1]['file_id']
    else:
        file_id = None
    if 'successful_payment' in data['message']:
        payment = True
    else:
        payment = None
    if 'text' in data['message']:
        message = data['message']['text']
    else:
        message = None
    return user_id, message, message_id, file_id, location, payment
