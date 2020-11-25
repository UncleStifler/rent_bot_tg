
from filters.message_processing import price_to_dict
from filters.message_processing import rooms_to_int


def delete_filter(user_state, user_id, data=None):
    user_state.filters[user_id].pop('filter', None)

def add_filter(user_state, user_id, data=None):
    user_state.add_user_filter(user_id)
    data = {
        'user_id': user_id,
        'name': 'Filter',
        'f_filter': {
            'type': None,
            'city': None,
            'district': None,
            'sex': None,
            'pets': None,
            'smoke': None,
            'owner': None,
            'rooms': None,
            'min_price': None,
            'max_price': None
        },
        'g_filter': None
    }
    user_state.filters[user_id] = {'filter': data}

def end_filter(user_state, user_id, data=None):
    print('end filter')
    delete_filter(user_state, user_id)


def type_(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1], f'type {data = } // [0, 1]'
    user_state.filters[user_id]['filter']['f_filter']['type'] = data

def rooms(user_state, user_id, data):
    if isinstance(data, str):
        data = rooms_to_int(data)
    assert isinstance(data, int), f'rooms {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['filter']['f_filter']['rooms'] = data

def price(user_state, user_id, data):
    if isinstance(data, str):
        data = price_to_dict(data)
    assert isinstance(data, dict), f' price {data = } >> dict'
    user_state.filters[user_id]['filter']['f_filter']['min_price'] = data['min_price']
    user_state.filters[user_id]['filter']['f_filter']['max_price'] = data['max_price']

def district(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'district {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['filter']['f_filter']['district'] = data

def route(user_state, user_id, data):
    data = {
        'route': data,
        'radius': 1
    }
    user_state.filters[user_id]['filter']['g_filter'] = data

def radius(user_state, user_id, data):
    data = float(data)
    assert isinstance(data, float), f'radius {data = } >> float'
    assert data > 0, f'radius {data = } < 0'
    user_state.filters[user_id]['filter']['g_filter']['radius'] = data

def sex(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'sex {data = } // [0, 1, 2]'
    user_state.filters[user_id]['filter']['f_filter']['sex'] = data

def pets(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'pets {data = } >> bool'
    user_state.filters[user_id]['filter']['f_filter']['pets'] = data

def smoke(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'smoke {data = } >> bool'
    user_state.filters[user_id]['filter']['f_filter']['smoke'] = data

def owner(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'owner {data = } >> bool'
    user_state.filters[user_id]['filter']['f_filter']['owner'] = data

def name(user_state, user_id, data):
    assert isinstance(data, str) and len(data) < 101, f'owner {data = } >> str, len < 100'
    user_state.filters[user_id]['filter']['name'] = data
    end_filter(user_state, user_id)