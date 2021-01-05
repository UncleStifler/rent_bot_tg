

import ui.lang_lines as ll
import ui.lang_buttons as lb

def donation_text(lang='en'):
    return 'Donation Text'

def donation_keyboard(lang='en', return_button=None):
    keyboard = {'inline_keyboard': [
    [{'text': 'Donation 5$', 'callback_data': 'donation-5'}]
    ]}
    if return_button:
        keyboard['inline_keyboard'].append(
            [{'text': 'Back', 'callback_data': return_button}]
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
        [{'text': 'Donation', 'callback_data': 'donation_menu-'}]
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