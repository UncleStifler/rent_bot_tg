
from db.asql import count_users
from db.asql import insert_statistic_record
from utils.utils import log_err

# types
# 1 - all_users
# 2 - active users

async def record_users_amount(pool, active_users: int):
    try:
        users_amount = (await count_users(pool))[0]['count']
        await insert_statistic_record(pool, users_amount, 1)
        await insert_statistic_record(pool, active_users, 2)
    except Exception as err:
        log_err(err)