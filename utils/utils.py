
import time

def get_current_timestamp():
    return int(time.time())

def is_old(last_update, time_update):
    return (int(time.time()) - last_update) > time_update