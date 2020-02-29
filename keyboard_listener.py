from pynput.keyboard import Key, Listener, KeyCode
from functions import value, key_string, activate_special_key_if_pressed, deactivate_special_key_if_released, combo, current_key, is_special_key_pressed, release_all_special_keys

combos = {}

# REVERT BACK TO NON-CLASS FOR IT TO WORK

class KeyboardListener:
    def __init__(self, combinations=combos):
        self.combos = combinations
        
    def on_press(self, key):
        key = key_string(key)
        global current_key
        global is_special_key_pressed
        current_key = key
        activate_special_key_if_pressed(key)
        for combination in self.combos.values():
            if combo(combination, current_key):
                release_all_special_keys()
                combination.execute()

    def on_release(self, key):
        key = key_string(key)
        deactivate_special_key_if_released(key)
        if key == 'esc':
            return False

    def run(self, on_press = on_press, on_release = on_release):
        with Listener(
                    on_press=self.on_press,
                    on_release=self.on_release) as l:
                l.join()    

class Combo:
    def __init__(self, special_keys, character, function, *args, **kwargs):
        self.special_keys = special_keys
        self.character = character
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def execute(self):
        self.function(*self.args, **self.kwargs)