
from backend.message_processing import price_to_dict
from backend.message_processing import rooms_to_int

# todo refactor

def delete_property(user_state, user_id, data=None):
    user_state.filters.pop(user_id, None)

def add_property(user_state, user_id, data=None):
    user_state.add_user_filter(user_id)
    data = {
        'user_id': user_id,
        'property': {
            'type': None,
            'city': 1,
            'district': None,
            'sex': None,
            'pets': None,
            'smoke': None,
            'owner': None,
            'rooms': None,
            'min_price': None,
            'max_price': None
        },
        'description': {
            'title': None,
            'description': None,
            'contact_name': None,
            'contact_phone': None,
            'photo': None
        }
    }
    user_state.filters[user_id] = data

def type_(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'type {data = } // [0, 1, 2]'
    if data == 2:
        data = None
    user_state.filters[user_id]['property']['type'] = data

def rooms(user_state, user_id, data):
    if isinstance(data, str):
        data = rooms_to_int(data)
    assert isinstance(data, int), f'rooms {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['rooms'] = data

def price(user_state, user_id, data):
    if isinstance(data, str):
        data = price_to_dict(data)
    assert isinstance(data, dict), f' price {data = } >> dict'
    user_state.filters[user_id]['property']['min_price'] = data['min_price']
    user_state.filters[user_id]['property']['max_price'] = data['max_price']

def district(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'district {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['district'] = data

def sex(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'sex {data = } // [0, 1, 2]'
    user_state.filters[user_id]['property']['sex'] = data

def pets(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'pets {data = } >> bool'
    user_state.filters[user_id]['property']['pets'] = data

def smoke(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'smoke {data = } >> bool'
    user_state.filters[user_id]['property']['smoke'] = data

def owner(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'owner {data = } >> bool'
    user_state.filters[user_id]['property']['owner'] = data

def title(user_state, user_id, data):
    user_state.filters[user_id]['description']['title'] = data

def description(user_state, user_id, data):
    user_state.filters[user_id]['description']['description'] = data

def contact_name(user_state, user_id, data):
    user_state.filters[user_id]['description']['contact_name'] = data

def contact_phone(user_state, user_id, data):
    user_state.filters[user_id]['description']['contact_phone'] = data

def photo(user_state, user_id, data):
    user_state.filters[user_id]['description']['photo'] = data