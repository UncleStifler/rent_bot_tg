
import aiohttp
import ujson

import config

ENDPOINT = f'http://{config.FILTER_APP_HOST}:{config.FILTER_APP_PORT}'


async def send_filter(data):
    url = ENDPOINT + '/add_filter/'
    return await _post_req(url,
                           data)


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