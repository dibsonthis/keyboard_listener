from keyboard_listener import KeyboardListener, Combo, KeyWord
from pynput.keyboard import Key, Controller
import pyperclip
import random
import time

keyboard = Controller()

def get_clipboard_data():
    data = pyperclip.paste()
    return data

def copy_to_clipboard(content):
    pyperclip.copy(content)

def clear_clipboard():
    pyperclip.copy('')

def copy_text():
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.1)

def paste_text():
    time.sleep(0.1)
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)

def delete(string):
    for char in string:
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    time.sleep(0.1)

def replace(old, new):
    copy_to_clipboard(new)
    delete(old)
    paste_text()
    

def modify(modification):
    modifications = {
        'upper': lambda data : data.upper(),
        'lower': lambda data : data.lower(),
        'cap_first': lambda data : data.capitalize(),
        'cap_all': lambda data : ' '.join([x.capitalize() for x in data.split(' ')]),
        'snake_case': lambda data : '_'.join([x.lower() for x in data.split(' ')]),
        'reverse': lambda data : data[::-1]
        }
    copy_text()
    data = get_clipboard_data()
    data = modifications[modification](data)
    print(data)
    copy_to_clipboard(data)
    paste_text()
    print(f'{modification} done')


combinations = {

        'combo1': Combo(['alt'], '1', modify, 'upper'),
        'combo2': Combo(['alt'], '2', modify, 'lower'),
        'combo3': Combo(['alt'], '3', modify, 'cap_first'),
        'combo4': Combo(['alt'], '4', modify, 'cap_all'),
        'combo5': Combo(['alt'], '5', modify, 'snake_case'),
        'combo6': Combo(['alt'], '6', modify, 'reverse')

}

keywords = {

    'help': KeyWord('--help', replace, '--help', 'Instead of this message, the function could instead alert emergency services 🚨🚨🚨'),
    'signature': KeyWord('--sig', replace, '--sig', 'Kind Regards\nJohn Smith from Generic Company'),
    '100': KeyWord('--100', replace, '--100', str([x for x in range(100)]))
}


keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
