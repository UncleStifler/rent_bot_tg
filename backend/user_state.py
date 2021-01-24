
import asyncio

import config
from db.asql import get_user
from db.asql import update_user
from db.asql import insert_user_ad
from backend.property_adding.utils import Property
from backend.statistic.users import record_users_amount
from utils.filters_api import send_filter
from utils.utils import get_current_timestamp
from utils.utils import is_old


class UserState:
    def __init__(self, pool):
        self.pool = pool
        self.state = {}
        self.filters = {}
        self.active_users = set()
        asyncio.ensure_future(self.init_cycle())
        asyncio.ensure_future(self.recording_statistics())

    async def recording_statistics(self):
        while True:
            await record_users_amount(self.pool,
                                      len(self.active_users))
            await asyncio.sleep(3600)

    # todo user.state for direct answers
    async def init_cycle(self):
        while True:
            if self.state:
                state_dict = self.state.copy()
                for user, values in state_dict.items():
                    if is_old(self.state[user]['last_update'],
                              config.USER_DATA_OLD_TIME) and not self.get_state(user):
                        await update_user(self.pool,
                                          user,
                                          values['message_id'],
                                          values['lang'])
                        self.state.pop(user, None)

            await asyncio.sleep(config.USER_DATA_UPDATE_TIME)

    async def add_user_state(self, user_id):
        self.active_users.add(user_id)
        db_user = await get_user(self.pool, user_id)
        if db_user:
            self.state[user_id] = {'message_id': db_user[0]['message_id'],
                                   'lang': db_user[0]['lang'],
                                   'last_update': get_current_timestamp()}
        else:
            self.state[user_id] = {'message_id': None,
                                   'lang': None,
                                   'last_update': get_current_timestamp()}

    async def change_message_id(self, user_id, id_):
        self.active_users.add(user_id)
        try:
            self.state[user_id]['message_id'] = id_
            self.state[user_id]['last_update'] = get_current_timestamp()
        except KeyError:
            await self.add_user_state(user_id)
            self.state[user_id]['message_id'] = id_
            self.state[user_id]['last_update'] = get_current_timestamp()

    async def change_state(self, user_id, name):
        self.active_users.add(user_id)
        try:
            self.state[user_id]['state'] = name
        except KeyError:
            await self.add_user_state(user_id)
            self.state[user_id]['state'] = name

    async def change_lang(self, user_id, lang):
        self.active_users.add(user_id)
        try:
            self.state[user_id]['lang'] = lang
        except KeyError:
            await self.add_user_state(user_id)
            self.state[user_id]['lang'] = lang

    async def get_message_id(self, user_id):
        self.active_users.add(user_id)
        try:
            return self.state[user_id]['message_id']
        except KeyError:
            await self.add_user_state(user_id)
            return self.state[user_id]['message_id']

    async def get_lang(self, user_id):
        self.active_users.add(user_id)
        try:
            return self.state[user_id]['lang']
        except KeyError:
            await self.add_user_state(user_id)
            return self.state[user_id]['lang']

    def get_state(self, user_id):
        self.active_users.add(user_id)
        try:
            return self.state[user_id]['state']
        except KeyError:
            return None

    def get_filter(self, user_id):
        self.active_users.add(user_id)
        try:
            return self.filters[user_id]
        except KeyError:
            return None

    # --------------------------------------------------------------------------

    def add_user_filter(self, user_id):
        self.active_users.add(user_id)
        self.filters[user_id] = {}

    def delete_user_filter(self, user_id):
        self.active_users.add(user_id)
        self.filters.pop(user_id, None)

    # errors will handle from main calling func
    async def send_to_filters(self, user_id, new=True):
        self.active_users.add(user_id)
        await send_filter(self.filters[user_id], new=new)
        self.filters.pop(user_id, None)

    async def send_property(self, user_id):
        self.active_users.add(user_id)
        property = Property(self.filters[user_id])
        await insert_user_ad(self.pool, property)
        self.filters.pop(user_id, None)

