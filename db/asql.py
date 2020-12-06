import asyncpg
import time

import config
import db.queries as q

async def get_pool():
	return await asyncpg.create_pool(user=config.DB_USER,
                                     password=config.DB_PASSWORD,
                                     database=config.DB_DATABASE,
                                     host=config.DB_HOST,)

# conn.execute or fetch
async def pool_req(pool, q):
	async with pool.acquire() as connection:
		async with connection.transaction():
			res = await connection.fetch(q)
			return res

async def get_districts(pool):
	return await pool_req(pool, q.districts())

async def get_routes(pool, route_type=1):
	return await pool_req(pool, q.routes(route_type))

async def get_user_filters(pool, user_id):
	return await pool_req(pool, q.get_user_filters(user_id))

async def get_filter_by_ids(pool, user_id, filter_id):
	return await pool_req(pool, q.get_filter(user_id, filter_id))

async def get_property_item(pool, filter_id, property_id):
	return await pool_req(pool, q.get_property_item(filter_id, property_id))


