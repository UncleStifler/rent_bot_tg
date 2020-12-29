import asyncio

import config
import db.asql as asql

# ((title, id), ..., ())
class DataUpdater:
    def __init__(self, pool):
        self.pool = pool
        self.districts = None
        self.metro_routes = None
        self.bus_routes = None
        asyncio.ensure_future(self.init_cycle())

    async def init_cycle(self):
        while True:
            self.cities = tuple(tuple((x['name'],
                                       x['id'])) for x in await asql.get_cities(self.pool))
            self.districts = tuple(tuple((x['name'],
                                          x['id'],
                                          x['city_id'])) for x in await asql.get_districts(self.pool))
            self.metro_routes = tuple(tuple((x['short_name'],
                                             x['id'])) for x in await asql.get_routes(self.pool, 1))
            self.bus_routes = tuple(tuple((x['short_name'],
                                           x['id'])) for x in await asql.get_routes(self.pool, 3))
            self.trains = tuple(tuple((x['short_name'],
                                           x['id'])) for x in await asql.get_routes(self.pool, 2))
            await asyncio.sleep(config.DATA_UPDATE_TIME)

    def get_districts(self, city_id):
        return tuple(x for x in self.districts if x[2] == city_id)