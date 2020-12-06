

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

# [[text, callback_data], ...]
def build_buttons(data):
    return [{'text': x[0], 'callback_data': x[1]} for x in data]

def build_common_keyboard(data,
                          data_callback,
                          buttons=None,
                          in_row=True):
    keyboard = _get_buttons(data, data_callback)
    if buttons:
        buttons_ = build_buttons(buttons)
        if in_row:
            keyboard['inline_keyboard'].append(buttons_)
        else:
            for b in buttons_:
                keyboard['inline_keyboard'].append([b])
    return keyboard

def search_bd(q, data):
    if q:
        for i in data:
            if i[1] == q:
                return i[0]


