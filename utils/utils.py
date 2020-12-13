
import time
import traceback
from loguru import logger


def get_current_timestamp():
    return int(time.time())

def is_old(last_update, time_update):
    return (int(time.time()) - last_update) > time_update

def log_err(err):
    tb = '\n'.join(traceback.format_tb(err.__traceback__))
    logger.error(f'\n{err}\n{tb}')
