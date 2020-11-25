import asyncpg

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
                                     host=config.DB_HOST)

# conn.execute or fetch

async def pool_reqs(queries):
	pool = await get_pool()
	async with pool.acquire() as connection:
		async with connection.transaction():
			for q in queries:
				await connection.fetch(q)


async def trans_req(q):
	connection = await get_conn()
	async with connection.transaction():
		return await connection.fetch(q)


async def get_districts():
	return await trans_req(q.districts())

async def get_routes(route_type=1):
	return await trans_req(q.routes(route_type))



