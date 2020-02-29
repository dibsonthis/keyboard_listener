from pynput.keyboard import Key, Controller
import pyperclip
import time

class Combo:
    def __init__(self, special_keys, character, function, *args, **kwargs):
        self.special_keys = special_keys
        self.character = character
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def execute(self):
        self.function(*self.args, **self.kwargs)

# Define combo functions here:

def change_case(case):
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
    print(f'changed to: {data}')
    pyperclip.copy(data)
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    print(f'pasted: {data}')
    print(f'{case} done')

# Insert combos here:

combos = {

'lowercase': Combo(['alt'], 'l', change_case, case='lower'),
'uppercase': Combo(['alt'], 'u', change_case, case='upper'),
'flip': Combo(['alt'], 'k', change_case, case='flip'),
'capitalize': Combo(['alt'], 'c', change_case, case='capitalize'),
'capitalize': Combo(['alt'], 'r', change_case, case='reverse')
}

