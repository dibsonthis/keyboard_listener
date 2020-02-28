from pynput.keyboard import Key, Listener, KeyCode
from combos import combos
from functions import value, key_string, activate_special_key_if_pressed, deactivate_special_key_if_released, combo, current_key, is_special_key_pressed

def on_press(key):
    key = key_string(key)
    global current_key
    global combos
    current_key = key
    activate_special_key_if_pressed(key)
    for combination in combos.values():
        # Need to fix to include ctrl --- ctrl+alt has different key code
        if combo(combination, current_key):
            combination[-1]()
    print(current_key)

def on_release(key):
    key = key_string(key)
    deactivate_special_key_if_released(key)
    if key == 'esc':
        return False
    print(is_special_key_pressed)

def run(on_press = on_press, on_release = on_release):
    with Listener(
                on_press=on_press,
                on_release=on_release) as l:
            l.join()    

run()                                    
                        
                           
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        