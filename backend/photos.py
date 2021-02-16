
import os
from aiohttp import web

import config
from utils.tg_api import get_file_path, FILE_URL
from utils.tg_api import download_file
from utils.utils import log_err


# async def photos_handler(request):
#     photo_id = request.match_info['photo_id']
#     try:
#         with open(f'{config.IMAGE_FOLDER}{photo_id}.jpg', 'rb') as f:
#             data = f.read()
#         return web.Response(body=data, content_type='image/jpeg')
#     except FileNotFoundError:
#         return web.Response(status=404)

async def process_file(file_id):
    data = await get_file_path(file_id)
    return file_id
    #№print('data', data)
    #try:
    #    file_path = data['result']['file_path']
    #    file_url = FILE_URL + file_path
    #    print(file_url)
        #data = await download_file(file_path)
        #id_ = get_filename()
        #print(id_)
        #with open(f'{config.IMAGE_FOLDER}{id_}.jpg', 'wb') as f:
            #f.write(data)
    #    return file_url
    #except Exception as err:
    #    log_err(err, data)
    #    return 'error'

def get_filename():
    return max([int(x.replace('.jpg', '')) for x in os.listdir(f'{config.IMAGE_FOLDER}')]) + 1

def get_photo_url(photo_id):
    if photo_id:
        if isinstance(photo_id, int):
            return f'https://{config.URL}/photos/{photo_id}.jpg'
        elif isinstance(photo_id, str):
            try:
                return get_photo_url(int(photo_id.split('/')[1]))
            except Exception as err:
                log_err(err, photo_id)
                return None
    else:
        return None