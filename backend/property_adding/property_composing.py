
from backend.message_processing import to_int


async def send_property(user_state, user_id, data=None):
    await user_state.send_property(user_id)

async def add_property(user_state, user_id, data=None):
    user_state.add_user_filter(user_id)
    data = {
        'user_id': user_id,
        'property': {
            'type': None,
            'city': None,
            'district': None,
            'sex': None,
            'pets': None,
            'smoke': None,
            'owner': None,
            'rooms_number': None,
            'price': None,
            'latitude': None,
            'longitude': None
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
    assert data in [0, 1], f'type {data = } // [0, 1]'
    user_state.filters[user_id]['property']['type'] = data

async def rooms(user_state, user_id, data):
    if isinstance(data, str):
        data = to_int(data)
    assert isinstance(data, int), f'rooms_number {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['rooms_number'] = data

async def geo(user_state, user_id, data):
    assert len(data) == 4, f'geo {data = } >> float'
    assert isinstance(data[2], float) and isinstance(data[3], float), f'geo {data = } >> float'
    assert isinstance(data[0], int) and isinstance(data[1], int), f'geo {data = } >> int'
    user_state.filters[user_id]['property']['city'] = data[0]
    user_state.filters[user_id]['property']['district'] = data[1]
    user_state.filters[user_id]['property']['latitude'] = data[2]
    user_state.filters[user_id]['property']['longitude'] = data[3]

async def price(user_state, user_id, data):
    if isinstance(data, str):
        data = to_int(data)
    assert isinstance(data, int), f'price {data = } >> int'
    assert data > 0, f'price {data = } <= 0'
    user_state.filters[user_id]['property']['price'] = data

async def city(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'city {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['city'] = data

async def district(user_state, user_id, data):
    data = int(data)
    assert isinstance(data, int), f'district {data = } >> int'
    if data == 0:
        data = None
    user_state.filters[user_id]['property']['district'] = data

async def sex(user_state, user_id, data):
    data = int(data)
    assert data in [0, 1, 2, 3], f'sex {data = } // [0, 1, 2, 3]'
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
    if data == '0':
        data = None
    user_state.filters[user_id]['description']['photo'] = data