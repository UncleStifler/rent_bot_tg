import asyncpg
import time

import config
import db.queries as q

async def get_conn():
	return await asyncpg.connect(user=config.DB_USER,
								 password=config.DB_PASSWORD,
								 database=config.DB_DATABASE,
								 host=config.DB_HOST)

async def get_pool():
	return await asyncpg.create_pool(user=config.DB_USER,
                                     password=config.DB_PASSWORD,
                                     database=config.DB_DATABASE,
                                     host=config.DB_HOST,)

# conn.execute or fetch

# 0.8-0.9 s
async def pool_req(pool, q):
	start = time.time()
	async with pool.acquire() as connection:
		async with connection.transaction():
			res = await connection.fetch(q)
			print(f'pool req - {time.time() - start} s')
			return res

# 0.12-0.3 s
async def trans_req(q):
	start = time.time()

	connection = await get_conn()
	async with connection.transaction():
		res = await connection.fetch(q)
		print(f'trans req - {time.time() - start} s')
		return res


async def get_districts(pool):
	return await pool_req(pool, q.districts())

async def get_routes(pool, route_type=1):
	return await pool_req(pool, q.routes(route_type))

async def get_user_filters(pool, user_id):
	return await pool_req(pool, q.get_user_filters(user_id))

async def get_filter_by_ids(pool, user_id, filter_id):
	return await pool_req(pool, q.get_filter(user_id, filter_id))


