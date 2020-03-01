# keyboard_listener

Keyboard Listener is a module that allows you to create custom hotkeys (combinations) or custom keywords and bind them to custom functions in Python. It's really easy to use and can be installed via pip:

`pip install keyboard_listener`

**Combinations** are custom hotkeys that are bound to functions. When the combination is pressed, the function is executed. Combos are really easy to set up and can be seen in the example below.

**Keywords** are custom strings that when entered (or rather, when their characters are entered in sequence) trigger a function to be executed. Keywords are also shown in the example below.

**KeyboardListener** object needs to be instantiated with the custom combinations and custom keywords dictionaries before running. Please refer to the below example to see how to set those up. If no dictionaries are passed, the program will assume no combinations or keywords are set up.

## Example:

```python
from keyboard_listener import KeyboardListener, Combo, KeyWord

def function_1(arguments):
  # do something
  
def function_2(arguments):
  # do something else

combinations = {

      'function 1': Combo(['alt'], 'f', function_1, arguments), 
        #Function 1 is executed when the user pressed Alt+F
      'function 2': Combo(['ctr','alt'], 'g', function_2, arguments), 
        #Function 2 is executed when the user pressed Alt+G
      'function 3': Combo(['shift','alt'], 'H', function_2, arguments), 
        #Be mindful when setting up Combos that include 'shift'. If the Combo includes the shift key, the character must be uppercase.
}

keywords = {

    'keyword_1': KeyWord('keyword1', function_1, arguments), 
      #Function 1 is executed when the user types 'keyword1'
    'keyword_2': KeyWord('keyword1', function_2, arguments) 
      #Function 2 is executed when the user types 'keyword2'
}

keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
```
