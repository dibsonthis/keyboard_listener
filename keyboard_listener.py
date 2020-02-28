from pynput.keyboard import Key, Listener

# ASCII characters found at https://donsnotes.com/tech/charsets/ascii.html

control_characters = {  'a':'\x01', 'b':'\x02', 'c':'\x03',
                        'd':'\x04', 'e':'\x05', 'f':'\x06', 
                        'g':'\x07', 'h':'\x08', 'i':'\x09',
                        'j':'\x0A', 'k':'\x0B', 'l':'\x0C',
                        'm':'\x0D', 'n':'\x0E', 'o':'\x0F',
                        'p':'\x10', 'q':'\x11', 'r':'\x12',
                        's':'\x13', 't':'\x14', 'u':'\x15',
                        'v':'\x16', 'w':'\x17', 'x':'\x18',
                        'y':'\x19', 'z':'\x1A', '[':'\x1B',
                        ']':'\x1D', '^':'\x1E', '_':'\x1F',
                        '?':'\x7F'}


def on_press(key):
    try:
        if key.char == control_characters['CTRL+H']:
            print('hello world')
        elif key.char == control_characters['CTRL+G']:
            print('goodbye world')
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        return False

def run(on_press, on_release):
    with Listener(
                on_press=on_press,
                on_release=on_release) as l:
            l.join()

run(on_press, on_release)
                        
                        
                        
                        
                           
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        