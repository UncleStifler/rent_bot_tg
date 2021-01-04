
import unicodedata


import config
from db.asql import get_geo

async def valid_geo(message, args):
    try:
        if isinstance(message, dict):
            lat, lon = message['latitude'], message['longitude']
        else:
            message = message.replace(' ', '').split('/')
            assert len(message) == 2, f'geo wrong {message = }'
            lat = float(message[0].replace(',', '.'))
            lon = float(message[1].replace(',', '.'))
        db_geo = await get_geo(args.pool, lat, lon)
        try:
            city_id = db_geo[0]['city_id']
            district_id = db_geo[0]['district']
            return [city_id, district_id, lat, lon]
        except IndexError:
            print(f'error: valid_geo - no match {message = }')
    except (ValueError, AssertionError) as err:
        print(f'error: valid_geo, {err}')

def _isascii(input_string):
    try:
        encoded_string = input_string.encode()
        return len(input_string) == len(encoded_string)
    except UnicodeEncodeError:
        return False

def toascii(input_string):
    try:
        return unicodedata.normalize('NFD', input_string).encode('ascii', 'ignore').decode('utf8')
    except Exception as err:
        print(err)
        return input_string

def photo_check(message):
    try:
        assert message.startswith('local/'), f'message is not photo {message = }'
        return message
    except AssertionError as err:
        print(f'error: photo, {err}')

def limit_string(message, limit=190):
    try:
        assert len(message) < limit, f'message is out of limit {message = }'
        message = toascii(message)
        assert _isascii(message), f'message is not ascii {message = }'
        return message
    except AssertionError as err:
        print(f'error: limit_string, {err}')

def limit_string_2000(message):
    return limit_string(message, limit=1900)

def limit_string_100(message):
    return limit_string(message, limit=95)

def price_to_dict(message):
    data = {
        'min_price': None,
        'max_price': None
    }
    message = message.replace(' ', '')
    try:
        assert len(message) < 30
        if '>' in message:
            price = message.split('>')
            assert len(price) == 2 and price[1].isdigit(), f'{price = }'
            data['min_price'] = int(price[1])
        elif '<' in message:
            price = message.split('<')
            assert len(price) == 2 and price[1].isdigit(), f'{price = }'
            data['max_price'] = int(price[1])
        elif '-' in message or '/' in message:
            if '-' in message:
                prices = message.split('-')
            else:
                prices = message.split('/')
            assert len(prices) == 2, f'{prices = }'
            data['min_price'], data['max_price'] = [int(x) for x in prices if x.isdigit()]
            assert data['min_price'] < data['max_price']
        else:
            if int(message) == 0:
                return data
            raise ValueError
        return data
    except (ValueError, AssertionError) as err:
        print(f'error: price_to_dict, {err}')

def to_int(message):
    try:
        assert len(message) < 4, f'len {message = }'
        assert message.isdigit(), f'digits {message = }'
        return int(message)
    except (ValueError, AssertionError) as err:
        print(f'error: rooms_to_int, {err}')

def price_to_int(message):
    try:
        assert len(message) < 7, f'len {message = }'
        assert message.isdigit(), f'digits {message = }'
        return int(message)
    except (ValueError, AssertionError) as err:
        print(f'error: price_to_int, {err}')

def auth_(message):
    try:
        assert message == config.ADMIN_PASSWORD, f'password invalid {message = }'
        return True
    except AssertionError as err:
        print(f'error: auth_, {err}')