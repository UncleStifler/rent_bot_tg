

import ui.lang_lines as ll
import ui.lang_buttons as lb

def donation_start(lang='en'):
    return ll.donation_start[lang]

def donation_keyboard(lang='en', return_button=None):
    keyboard = {'inline_keyboard': [
    [{'text': '1€', 'callback_data': 'donation-1'},
     {'text': '2€', 'callback_data': 'donation-2'}],
    [{'text': '5€', 'callback_data': 'donation-5'},
     {'text': '10€', 'callback_data': 'donation-10'}]
    ]}
    if return_button:
        keyboard['inline_keyboard'].append(
            [{'text': lb.back[lang], 'callback_data': return_button}]
        )
    return keyboard

def main_menu_text(lang='en'):
    return ll.main_menu_text[lang]
def main_menu_keyboard(lang='en'):
    return {'inline_keyboard': [
        [{'text': lb.add_filter[lang], 'callback_data': 'f_start-'}],
        [{'text': lb.my_filters[lang], 'callback_data': 'user_filters-'}],
        [{'text': lb.add_property[lang], 'callback_data': 'u_start_page-'}],
        [{'text': lb.select_lang[lang], 'callback_data': 'select_lang-'}],
        [{'text': lb.donation_button[lang], 'callback_data': 'donation_menu-'}]
    ]}

def lang_select_text(lang='en'):
    return ll.lang_select[lang]
def lang_select_keyboard(lang='en'):
    return {'inline_keyboard': [
        [{'text': 'English', 'callback_data': 'lang-en'}],
        [{'text': 'Español', 'callback_data': 'lang-es'}],
        [{'text': 'Русский', 'callback_data': 'lang-ru'}]
    ]}

def empty_result(lang='en'):
    return ll.empty_results[lang]


def back_menu_keyboard(lang='en'):
    return {'inline_keyboard': [
    [{'text': lb.main_menu[lang], 'callback_data': 'main_menu-'}]
    ]}
def f_error_text(lang='en'):
    return ll.f_error_text[lang]