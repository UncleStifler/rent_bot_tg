
import aiohttp
import ujson

import config

ENDPOINT = f'http://{config.FILTER_APP_HOST}:{config.FILTER_APP_PORT}'


async def send_filter(data, new=True):
    if new:
        url = ENDPOINT + '/add_filter/'
    else:
        url = ENDPOINT + '/change_filter/'
    return await _post_req(url, data)

async def delete_filter(filter_id):
    data = {'filter_id': filter_id}
    url = ENDPOINT + '/delete_filter/'
    return await _post_req(url, data)

async def send_show_more(filter_id):
    data = {'user_filter_id': filter_id}
    url = ENDPOINT + '/show_more/'
    return await _post_req(url, data)

async def delete_user(user_id):
    data = {'user_id': user_id}
    url = ENDPOINT + '/delete_user/'
    return await _post_req(url, data)

#[[<Record property_id=7603>], ..., [<Record property_id=7626>]]
async def send_new_ids(ids):
    data = {'ids': [x['id'] for x in ids]}
    url = ENDPOINT + '/new_ids/'
    return await _post_req(url, data)

async def _post_req(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url,
                                data=ujson.dumps(data)
                                ) as resp:
            try:
                assert resp.status == 200
                response = await resp.text()
                return response
            except Exception as err:
                print(err)
                print(await resp.text())
                return False