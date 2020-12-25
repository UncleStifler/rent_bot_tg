
import os
from aiohttp import web

import config
from utils.tg_api import get_file_path
from utils.tg_api import download_file

# todo if file deleted invalid name
def get_filename():
    return len(os.listdir(f'{config.IMAGE_FOLDER}/')) + 1

async def photos_handler(request):
    print(request)
    photo_id = request.match_info['photo_id']
    try:
        with open(f'{config.IMAGE_FOLDER}/{photo_id}.jpg', 'rb') as f:
            data = f.read()
        return web.Response(body=data, content_type='image/jpeg')
    except FileNotFoundError:
        return web.Response(status=404)

async def process_file(file_id):
    print(file_id)
    data = await get_file_path(file_id)
    try:
        file_path = data['result']['file_path']
        data = await download_file(file_path)
        id_ = get_filename()
        with open(f'{config.IMAGE_FOLDER}/{id_}.jpg', 'wb') as f:
            f.write(data)
        return f'local/{id_}'
    except Exception as err:
        print(err)
        return False