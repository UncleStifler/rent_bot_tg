
import scheme

def get_callback(data):
    user_id = data['callback_query']['message']['chat']['id']
    callback, callback_data = data['callback_query']['data'].split('-')
    if any(callback.startswith(x) for x in scheme.callback_w_pages):
        try:
            splited_callback = callback.split('/')
            callback = splited_callback[0]
            page = int(splited_callback[1])
        except IndexError:
            page = 0
    else:
        page = None
    return user_id, callback, callback_data, page

def get_message(data):
    user_id = data['message']['chat']['id']
    message = data['message']['text']
    message_id = data['message']['message_id']
    return user_id, message, message_id

def get_slice(data, page, slice=8):
    start = page*slice
    end = start + slice
    try:
        return data[start:end]
    except IndexError:
        return data[start:]

def get_buttons(data, callback, columns=3):
    keyboard = {'inline_keyboard': []}
    page = 0
    while True:
        slices = get_slice(data, page, slice=columns)
        if slices:
            row = [{'text': x[0], 'callback_data': f'{callback}-{x[1]}'} for x in slices]
            keyboard['inline_keyboard'].append(row)
            page += 1
        else:
            break
    return keyboard

def build_keyboard(data, page, data_callback, menu_callback, skip=True):
    keyboard = get_buttons(get_slice(data, page),
                           data_callback)
    control_buttons = []
    if page > 0:
        back_button = {'text': 'Back',
                       'callback_data': f'{menu_callback}/{page - 1}-'}
        control_buttons.append(back_button)
    next_data = get_slice(data, page + 1)
    if next_data:
        next_button = {'text': 'Next',
                       'callback_data': f'{menu_callback}/{page + 1}-'}
        control_buttons.append(next_button)
    keyboard['inline_keyboard'].append(control_buttons)
    if skip:
        keyboard['inline_keyboard'].append([{'text': "Doesn't matter",
                                             'callback_data': f'{data_callback}-0'}])
    return keyboard



