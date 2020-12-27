
import time
import traceback
from loguru import logger


def get_current_timestamp():
    return int(time.time())

def is_old(last_update, time_update):
    return (int(time.time()) - last_update) > time_update

def get_last_sec():
    return str(int(time.time()))[-2:]

def log_err(err, message=''):
    tb = '\n'.join(traceback.format_tb(err.__traceback__))
    text = f'\n{err}\n{message}\n{tb}'
    logger.error(text)
