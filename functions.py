from pynput.keyboard import KeyCode, Key, Controller
from special_characters import control_characters, alt_characters

current_key = None

is_special_key_pressed = {'ctrl':False, 'shift':False, 'alt':False, 'cmd':False}

recent_input = []

def value(key):
    try:
        return key.char
    except AttributeError:
        return str(key).replace('Key.', '')

def key_string(key):
    key = str(KeyCode.from_char(key))
    key = key.replace('Key.', '').replace('"','')
    key = eval(key)
    return key

def release_all_special_keys():
    keyboard = Controller()
    special_keys = [Key.ctrl_l, Key.ctrl_r, Key.ctrl, Key.shift, Key.shift_r, Key.alt, Key.alt_l, Key.alt_r]
    for key in special_keys:
        keyboard.release(key)

def activate_special_key_if_pressed(key):
    global is_special_key_pressed
    if value(key) == 'ctrl_l' or value(key) == 'ctrl_r':
        is_special_key_pressed['ctrl'] = True
    elif value(key) == 'shift' or value(key) == 'shift_r':
        is_special_key_pressed['shift'] = True
    elif value(key) == 'alt_l' or value(key) == 'alt_r':
        is_special_key_pressed['alt'] = True
    elif value(key) == 'cmd' or value(key) == 'cmd_l' or value(key) == 'cmd_r':
        is_special_key_pressed['cmd'] = True

def deactivate_special_key_if_released(key):
    global is_special_key_pressed
    if value(key) == 'ctrl_l' or value(key) == 'ctrl_r':
        is_special_key_pressed['ctrl'] = False
    elif value(key) == 'shift' or value(key) == 'shift_r':
        is_special_key_pressed['shift'] = False
    elif value(key) == 'alt_l' or value(key) == 'alt_r':
        is_special_key_pressed['alt'] = False
    elif value(key) == 'cmd' or value(key) == 'cmd_l' or value(key) == 'cmd_r':
        is_special_key_pressed['cmd'] = False

def combo(combination, current_key=current_key):
    special_keys = combination.special_keys
    character = combination.character
    if 'ctrl' in special_keys and 'alt' not in special_keys:
        character = control_characters[character]
    if 'ctrl' in special_keys and 'alt' in special_keys:
        character = alt_characters[character]
    if all( is_special_key_pressed[x] for x in special_keys ) and current_key == character:
        return True


