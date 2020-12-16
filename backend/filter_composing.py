
from backend.message_processing import price_to_dict
from backend.message_processing import to_int

async def delete_filter(user_state, user_id, data=None):
    user_state.filters.pop(user_id, None)

async def add_filter(user_state, user_id, data=None):
    user_state.add_user_filter(user_id)
    if data:
        data = {
            'id': data['id'],
            'user_id': user_id,
            'name': data['name'],
            'f_filter': {
                'type': data['type'],
                'city': data['city'],
                'district': data['district'],
                'sex': data['sex'],
                'pets': data['pets'],
                'smoke': data['smoke'],
                'owner': data['owner'],
                'rooms': data['rooms'],
                'min_price': data['min_price'],
                'max_price': data['max_price']
            },
            'g_filter': {
                'route': data['route_id'],
                'radius': data['radius']
            }
        }
    else:
        data = {
            'id': None,
            'user_id': user_id,
            'name': 'Filter',
            'f_filter': {
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
            'g_filter': {
                'route': None,
                'radius': 1.0
            }
        }
    user_state.filters[user_id] = data

async def end_filter(user_state, user_id, data=None):
    await user_state.send_to_filters(user_id)

async def change_filter(user_state, user_id, data=None):
    await user_state.send_to_filters(user_id, new=False)

async def type_(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'type {data = } // [0, 1, 2]'
    if data == 2:
        data = None
    user_state.filters[user_id]['f_filter']['type'] = data

async def rooms(user_state, user_id, data):
    if isinstance(data, str):
        data = to_int(data)
    assert isinstance(data, int), f'rooms {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['f_filter']['rooms'] = data

async def price(user_state, user_id, data):
    if isinstance(data, str):
        data = price_to_dict(data)
    assert isinstance(data, dict), f' price {data = } >> dict'
    user_state.filters[user_id]['f_filter']['min_price'] = data['min_price']
    user_state.filters[user_id]['f_filter']['max_price'] = data['max_price']

async def district(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'district {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['f_filter']['district'] = data

async def route(user_state, user_id, data):
    data = int(data)
    data = {
        'route': data,
        'radius': 1.0
    }
    user_state.filters[user_id]['g_filter'] = data

async def radius(user_state, user_id, data):
    data = float(data)
    assert isinstance(data, float), f'radius {data = } >> float'
    assert data > 0, f'radius {data = } < 0'
    user_state.filters[user_id]['g_filter']['radius'] = data

async def sex(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'sex {data = } // [0, 1, 2]'
    user_state.filters[user_id]['f_filter']['sex'] = data

async def pets(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'pets {data = } >> bool'
    user_state.filters[user_id]['f_filter']['pets'] = data

async def smoke(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'smoke {data = } >> bool'
    user_state.filters[user_id]['f_filter']['smoke'] = data

async def owner(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'owner {data = } >> bool'
    user_state.filters[user_id]['f_filter']['owner'] = data

async def name(user_state, user_id, data):
    assert isinstance(data, str) and len(data) < 101, f'owner {data = } >> str, len < 100'
    user_state.filters[user_id]['name'] = data
    # await end_filter(user_state, user_id)