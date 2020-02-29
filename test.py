from keyboard_listener import KeyboardListener, Combo
from pynput.keyboard import Key, Controller
import pyperclip
import time

def modify_text(case):
    keyboard = Controller()
    data = pyperclip.paste()
    print(f'current: {data}')
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.1)
    data = pyperclip.paste()
    print(f'copied: {data}')

    if case == 'upper':
        data = data.upper()
    elif case == 'lower':
        data = data.lower()
    elif case == 'capitalize':
        data = data.capitalize()
    elif case == 'flip':
        data = ''.join([x.capitalize() if x == x.lower() else x.lower() for x in data])
    elif case == 'reverse':
        data = data[::-1]
    elif case == 'capitalize_every_word':
        data = data.split(' ')
        data = [x.capitalize() for x in data]
        data = ' '.join(data)
    elif case == 'alternate':
        data = [x for x in data]
        for index, character in enumerate(data):
            if index % 2 == 0:
                data[index] = character.upper()
            else:
                data[index] = character.lower()
        data = ''.join(data)
    elif case == 'eval':
        try:
            data = eval(data)
        except:
            data = data

    print(f'changed to: {data}')
    pyperclip.copy(data)
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    print(f'pasted: {data}')
    print(f'{case} done')

combinations = {

'lowercase': Combo(['alt'], 'l', modify_text, case='lower'),
'uppercase': Combo(['alt'], 'u', modify_text, case='upper'),
'flip': Combo(['alt'], 'k', modify_text, case='flip'),
'capitalize': Combo(['alt'], 'c', modify_text, case='capitalize'),
'reverse': Combo(['alt'], 'r', modify_text, case='reverse'),
'capitalize_every_word': Combo(['alt'], 'g', modify_text, case='capitalize_every_word'),
'alternate': Combo(['alt'], 'a', modify_text, case='alternate'),
'evaluate': Combo(['alt'], ']', modify_text, case='eval')
}


keyboard_listener = KeyboardListener(combinations=combinations)
keyboard_listener.run()