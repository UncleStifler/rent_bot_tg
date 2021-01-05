import asyncpg
import time

import config
import db.queries as q

async def get_pool(host=config.DB_HOST):
	return await asyncpg.create_pool(user=config.DB_USER,
                                     password=config.DB_PASSWORD,
                                     database=config.DB_DATABASE,
                                     host=host)

# conn.execute or fetch
async def pool_req(pool, q):
	async with pool.acquire() as connection:
		async with connection.transaction():
			try:
				res = await connection.fetch(q)
				return res
			except Exception as err:
				print(err)
				print(q)

# --------------------------------------------------------------------------

async def update_user(pool, user_id, message_id=None, lang=None):
	return await pool_req(pool, q.update_user(user_id, message_id, lang))

async def get_user(pool, user_id):
	return await pool_req(pool, q.get_user(user_id))

# --------------------------------------------------------------------------

async def get_cities(pool):
	return await pool_req(pool, q.cities())

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

async def insert_user_ad(pool, property):
	return await pool_req(pool, q.insert_user_ad(property))

async def get_last_user_ad(pool):
	return await pool_req(pool, q.get_last_user_ad())

async def delete_user_ad(pool, ad_id):
	return await pool_req(pool, q.delete_user_ad(ad_id))

async def insert_user_ad_to_db(pool, ad_id):
	timestamp = int(time.time())
	return await pool_req(pool, q.insert_ad_in_db(ad_id, timestamp))

async def get_geo(pool, lat, lon):
	return await pool_req(pool, q.get_city_and_district_by_geo(lat, lon))

async def get_users(pool, lang=None):
	return await pool_req(pool, q.get_users(lang))