


def _get_slice(data, page, slice=8):
    start = page*slice
    end = start + slice
    try:
        return data[start:end]
    except IndexError:
        return data[start:]

def _get_buttons(data, callback, columns=3):
    keyboard = {'inline_keyboard': []}
    if data and callback:
        page = 0
        while True:
            slices = _get_slice(data, page, slice=columns)
            if slices:
                row = [{'text': x[0], 'callback_data': f'{callback}-{x[1]}'} for x in slices]
                keyboard['inline_keyboard'].append(row)
                page += 1
            else:
                break
    return keyboard

def build_page_keyboard(data, page, data_callback, menu_callback, skip=True):
    keyboard = _get_buttons(_get_slice(data, page),
                            data_callback)
    control_buttons = []
    if page > 0:
        back_button = {'text': 'Back',
                       'callback_data': f'{menu_callback}/{page - 1}-'}
        control_buttons.append(back_button)
    next_data = _get_slice(data, page + 1)
    if next_data:
        next_button = {'text': 'Next',
                       'callback_data': f'{menu_callback}/{page + 1}-'}
        control_buttons.append(next_button)
    keyboard['inline_keyboard'].append(control_buttons)
    if skip:
        keyboard['inline_keyboard'].append([{'text': "Doesn't matter",
                                             'callback_data': f'{data_callback}-0'}])
    return keyboard

def build_common_keyboard(data, data_callback, back_title, back_callback):
    keyboard = _get_buttons(data, data_callback)
    keyboard['inline_keyboard'].append([{'text': back_title,
                                         'callback_data': f'{back_callback}-'}])
    return keyboard

def _search_bd(q, data):
    if q:
        for i in data:
            if i[1] == q:
                return i[0]

def filter_to_ui(filter, db):
    filter = filter[0]
    type_ = 'flats' if filter['type'] == 0 else 'rooms'
    city = 'Barcelona'
    district = _search_bd(filter['district'], db.districts)
    address = ' in '
    if district:
        address += f'{district}, {city}'
    else:
        address += city
    text = f'Filter - {filter["name"]}\nSearching {type_}{address}'

    if filter['rooms']:
        rooms = f'{filter["rooms"]} rooms'
    else:
        rooms = None

    if filter['min_price'] and filter['max_price']:
        price = f'between {filter["min_price"]} and {filter["max_price"]}'
    elif filter['min_price']:
        price = f'above {filter["min_price"]}'
    elif filter['max_price']:
        price = f'under {filter["max_price"]}'
    else:
        price = None

    if rooms and price:
        rooms_price = f'{rooms} with a price {price} euros'
    elif rooms:
        rooms_price = rooms
    elif price:
        rooms_price = f'With a price {price} euros'
    else:
        rooms_price = None

    if rooms_price:
        text += f'\n{rooms_price}'

    #todo routes
    return text

