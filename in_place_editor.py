from keyboard_listener import KeyboardListener, Combo, Input
from pynput.keyboard import Key, Controller
import pyperclip
import time

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

combinations = {

'lowercase': Combo(['alt'], 'l', modify_text, modification='lower'),
'uppercase': Combo(['alt'], 'u', modify_text, modification='upper'),
'flip': Combo(['alt'], 'k', modify_text, modification='flip'),
'capitalize': Combo(['alt'], 'c', modify_text, modification='capitalize'),
'reverse': Combo(['alt'], 'r', modify_text, modification='reverse'),
'capitalize_every_word': Combo(['alt'], 'g', modify_text, modification='capitalize_every_word'),
'alternate': Combo(['alt'], 'a', modify_text, modification='alternate'),
'evaluate': Combo(['alt'], ']', modify_text, modification='eval')
}

inputs = {

    'test': Input('help', print, 'HELP ME')
}


keyboard_listener = KeyboardListener(combinations=combinations, inputs=inputs)
keyboard_listener.run()