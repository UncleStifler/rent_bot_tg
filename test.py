
# second test commit

state = {2452: {}}

def add_user_state(user_id):
    state[user_id] = {}

def change_message_id(user_id, id_):
    def defs(user_id, id_): state[user_id]['message_id'] = id_


def key_error_handle(func):
    try:
        func()
    except KeyError:
        add_user_state(user_id)
        func()

change_message_id(425, 4534)
print(state)