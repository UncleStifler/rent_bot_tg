


class UserState:
    def __init__(self):
        self.state = {}
        self.filters = {}

    def add_user_state(self, user_id):
        if user_id not in self.state:
            self.state[user_id] = {}

    def add_user_filter(self, user_id):
        if user_id not in self.filters:
            self.filters[user_id] = {}

    def change_message_id(self, user_id, id_):
        self.add_user_state(user_id)
        self.state[user_id]['current_message'] = id_

    def get_message_id(self, user_id):
        try:
            return self.state[user_id]['current_message']
        except KeyError:
            return None

    def change_state(self, user_id, name):
        self.add_user_state(user_id)
        self.state[user_id]['state'] = name

    def get_state(self, user_id):
        try:
            return self.state[user_id]['state']
        except KeyError:
            return None

