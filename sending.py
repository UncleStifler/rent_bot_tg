
import asyncio

import config
from db.asql import (get_pool,
                     get_users)
from utils.tg_api import send_message



# markdown True

url = 'https://www.vippng.com/png/detail/101-1019439_maintenance-repair-24-appliance-repair-logo-png.png'
photo = f'[\u200B]({url})'

text = f'''
Dear users
We have some technical server side works.
Thank you for your patience
{photo}'''


async def main():
    pool = await get_pool(host=config.EXT_IP)
    users = await get_users(pool)
    user_ids = [x['id'] for x in users]
    await asyncio.wait([
        send_message(x, text) for x in user_ids
    ])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
