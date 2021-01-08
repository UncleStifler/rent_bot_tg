
import ujson

from utils.filters_api import delete_user
from utils.utils import log_err

def read_exception(data):
    try:
        message = ujson.loads(data)
        if message["description"] == 'Forbidden: bot was blocked by the user':
            return BotBlocked()
    except Exception as err:
        log_err(err, data)

class TelegramException():
    pass

class BotBlocked(TelegramException):
    async def process(self, user_id):
        await delete_user(user_id)