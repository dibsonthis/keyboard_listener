from keyboard_listener import KeyboardListener, Combo, KeyWord
from pynput.keyboard import Key, Controller
from functions import recent_input, current_key
import pyperclip
import time
import random

def get_clipboard_data():
    data = pyperclip.paste()
    return data

def copy_to_clipboard(content):
    pyperclip.copy(content)

def clear_clipboard():
    pyperclip.copy('')

def copy_text():
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.01)

def paste_text():
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)

def delete(string):
    keyboard = Controller()
    for char in string:
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.01)

def replace(old, new):
    pyperclip.copy(new)
    delete(old)
    paste_text()
    keyboard = Controller()
    keyboard.press(Key.shift)
    for char in new:
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    keyboard.release(Key.shift)

def is_digit(direction):
    keyboard = Controller()
    keyboard.press(Key.shift)
    if direction == 'left':
        keyboard.press(Key.left)
    elif direction == 'right':
        keyboard.press(Key.right)
    keyboard.release(Key.shift)
    copy_text()
    char = get_clipboard_data()
    if direction == 'left':
        keyboard.press(Key.left)
    elif direction == 'right':
        keyboard.press(Key.right)
    try:
        int(char)
        return True
    except ValueError:
        return False

def range_list(replacement):
    keys = []
    keyboard = Controller()
    for char in ']range':
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    while is_digit('left'):
        char = get_clipboard_data()
        keys.append(char)
    keys.reverse()
    keys = int(''.join(keys))
    result = ', '.join([str(x) for x in range(keys)])
    replacement = '[' + str(keys) + replacement
    print(replacement)
    keyboard.press(Key.shift)
    for char in replacement:
        keyboard.press(Key.right)
        time.sleep(0.01)
    keyboard.release(Key.shift)
    copy_to_clipboard(result)
    paste_text()

def modify_text(modification):
    data = get_clipboard_data()
    print(f'current: {data}')
    copy_text()
    data = get_clipboard_data()
    print(f'copied: {data}')

    if modification == 'upper':
        data = data.upper()
    elif modification == 'lower':
        data = data.lower()
    elif modification == 'capitalize':
        data = data.capitalize()
    elif modification == 'flip':
        data = ''.join([x.capitalize() if x == x.lower() else x.lower() for x in data])
    elif modification == 'reverse':
        data = data[::-1]
    elif modification == 'capitalize_every_word':
        data = data.split(' ')
        data = [x.capitalize() for x in data]
        data = ' '.join(data)
    elif modification == 'alternate':
        data = [x for x in data]
        for index, character in enumerate(data):
            if index % 2 == 0:
                data[index] = character.upper()
            else:
                data[index] = character.lower()
        data = ''.join(data)
    elif modification == 'spongebob':
        data = [x for x in data]
        for index, character in enumerate(data):
            data[index] = random.choice([character.upper(), character.lower()])
        data = ''.join(data)
    elif modification == 'eval':
        try:
            data = eval(data)
        except:
            data = data
    elif modification == 'snake_case':
        data = data.split(' ')
        data = [x.lower() for x in data]
        data = '_'.join(data)

    print(f'changed to: {data}')
    copy_to_clipboard(data)
    paste_text()
    keyboard = Controller()
    keyboard.press(Key.shift)
    for char in data:
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    keyboard.release(Key.shift)
    print(f'pasted: {data}')
    print(f'{modification} done')


combinations = {

'lowercase': Combo(['alt'], 'l', modify_text, modification='lower'),
'uppercase': Combo(['alt'], 'u', modify_text, modification='upper'),
'flip': Combo(['alt'], 'k', modify_text, modification='flip'),
'capitalize': Combo(['alt'], 'c', modify_text, modification='capitalize'),
'reverse': Combo(['alt'], 'r', modify_text, modification='reverse'),
'capitalize_every_word': Combo(['alt'], 'g', modify_text, modification='capitalize_every_word'),
'alternate': Combo(['alt'], 'a', modify_text, modification='alternate'),
'spongebob': Combo(['alt'], 'b', modify_text, modification='spongebob'),
'snake_case': Combo(['alt'], 'm', modify_text, modification='snake_case'),
'evaluate': Combo(['alt'], ']', modify_text, modification='eval')
}

keywords = {

    'help': KeyWord('--help', replace, '--help', 'Instead of this message, the function could instead alert emergency services 🚨🚨🚨'),
    'range': KeyWord(']range', range_list, ']range')
}


keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
