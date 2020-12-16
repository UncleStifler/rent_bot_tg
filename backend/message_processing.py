

def _isascii(input_string):
    try:
        encoded_string = input_string.encode()
        return len(input_string) == len(encoded_string)
    except UnicodeEncodeError:
        return False

def limit_string(message, limit=200):
    try:
        assert len(message) < limit, f'message is out of limit {message = }'
        assert _isascii(message), f'message is not ascii {message = }'
        return message
    except AssertionError as err:
        print(f'error: limit_string, {err}')
        return None

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
        return None

def to_int(message):
    try:
        assert len(message) < 4, f'len {message = }'
        assert message.isdigit(), f'digits {message = }'
        return int(message)
    except (ValueError, AssertionError) as err:
        print(f'error: rooms_to_int, {err}')
        return None

def name_to_str(message):
    try:
        assert len(message) < 101, f'len {message = }'
        assert _isascii(message), f'not ascii {message = }'
        return message
    except (ValueError, AssertionError) as err:
        print(f'error: name_to_str, {err}')
        return None