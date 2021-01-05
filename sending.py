
import asyncio

import config
from db.asql import (get_pool,
                     get_users)
from utils.tg_api import send_message



# markdown True

photo = '[\u200B](https://www.vippng.com/png/detail/101-1019439_maintenance-repair-24-appliance-repair-logo-png.png)'

text = f'''
Dear users
The server is undergoing technical work until 01:00 UTC. The bot may not work correctly. We ask you to refrain from actively interacting with the search.
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
