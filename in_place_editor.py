from keyboard_listener import KeyboardListener, Combo, KeyWord
from pynput.keyboard import Key, Controller
import pyperclip
import time
import random

def copy_text():
    keyboard = Controller()
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.1)

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
        time.sleep(0.05)

def modify_text(modification):
    data = pyperclip.paste()
    print(f'current: {data}')
    copy_text()
    data = pyperclip.paste()
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

    print(f'changed to: {data}')
    pyperclip.copy(data)
    paste_text()
    print(f'pasted: {data}')
    print(f'{modification} done')

def help_function():
    pyperclip.copy(' *Instead of printing this message, the function could call emergency services*')
    paste_text()

def replace(old, new):
    pyperclip.copy(new)
    delete(old)
    paste_text()

combinations = {

'lowercase': Combo(['alt'], 'l', modify_text, modification='lower'),
'uppercase': Combo(['alt'], 'u', modify_text, modification='upper'),
'flip': Combo(['alt'], 'k', modify_text, modification='flip'),
'capitalize': Combo(['alt'], 'c', modify_text, modification='capitalize'),
'reverse': Combo(['alt'], 'r', modify_text, modification='reverse'),
'capitalize_every_word': Combo(['alt'], 'g', modify_text, modification='capitalize_every_word'),
'alternate': Combo(['alt'], 'a', modify_text, modification='alternate'),
'spongebob': Combo(['alt'], 'b', modify_text, modification='spongebob'),
'evaluate': Combo(['alt'], ']', modify_text, modification='eval')
}

keywords = {

    'signature': KeyWord('-sig', replace, '-sig', 'Kind Regards,\nJohn from Apple Sales Department'),
    'code-4544': KeyWord('-4544', replace, '-4544', 'Product Code: 4544\nProduct Name: Apple Mac II\nProduct Price: $544.95')
}


keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
