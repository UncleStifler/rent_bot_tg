import asyncio

import config
from db.asql import get_districts
from db.asql import get_routes

# ((title, id), ..., ())
class DataUpdater:
    def __init__(self):
        self.districts = None
        self.metro_routes = None
        self.bus_routes = None
        asyncio.ensure_future(self.init_cycle())

    async def init_cycle(self):
        while True:
            self.districts = tuple(tuple((x['name'], x['id'])) for x in await get_districts())
            self.metro_routes = tuple(tuple((x['short_name'], x['id'])) for x in await get_routes(1))
            self.bus_routes = tuple(tuple((x['short_name'], x['id'])) for x in await get_routes(3))
            await asyncio.sleep(config.DATA_UPDATE_TIME)
