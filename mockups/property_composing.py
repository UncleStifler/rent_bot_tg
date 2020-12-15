
from backend.message_processing import price_to_dict
from backend.message_processing import rooms_to_int

# todo refactor

async def delete_property(user_state, user_id, data=None):
    user_state.filters.pop(user_id, None)

async def add_property(user_state, user_id, data=None):
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

async def type_(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'type {data = } // [0, 1, 2]'
    if data == 2:
        data = None
    user_state.filters[user_id]['property']['type'] = data

async def rooms(user_state, user_id, data):
    if isinstance(data, str):
        data = rooms_to_int(data)
    assert isinstance(data, int), f'rooms {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['rooms'] = data

async def price(user_state, user_id, data):
    if isinstance(data, str):
        data = price_to_dict(data)
    assert isinstance(data, dict), f' price {data = } >> dict'
    user_state.filters[user_id]['property']['min_price'] = data['min_price']
    user_state.filters[user_id]['property']['max_price'] = data['max_price']

async def district(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'district {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['district'] = data

async def sex(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2], f'sex {data = } // [0, 1, 2]'
    user_state.filters[user_id]['property']['sex'] = data

async def pets(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'pets {data = } >> bool'
    user_state.filters[user_id]['property']['pets'] = data

async def smoke(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'smoke {data = } >> bool'
    user_state.filters[user_id]['property']['smoke'] = data

async def owner(user_state, user_id, data):
    data = bool(int(data))
    assert isinstance(data, bool), f'owner {data = } >> bool'
    user_state.filters[user_id]['property']['owner'] = data

async def title(user_state, user_id, data):
    user_state.filters[user_id]['description']['title'] = data

async def description(user_state, user_id, data):
    user_state.filters[user_id]['description']['description'] = data

async def contact_name(user_state, user_id, data):
    user_state.filters[user_id]['description']['contact_name'] = data

async def contact_phone(user_state, user_id, data):
    user_state.filters[user_id]['description']['contact_phone'] = data

async def photo(user_state, user_id, data):
    user_state.filters[user_id]['description']['photo'] = data