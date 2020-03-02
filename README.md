# keyboard_listener

Keyboard Listener is a module that allows you to create custom hotkeys (combinations) or custom keywords and bind them to custom functions in Python.

**Combinations** are custom hotkeys that are bound to functions. When the combination is pressed, the function is executed. Combos are really easy to set up and can be seen in the example below.

**Keywords** are custom strings that when entered (or rather, when their characters are entered in sequence) trigger a function to be executed. Keywords are also shown in the example below.

**KeyboardListener** object needs to be instantiated with the custom combinations and custom keywords dictionaries before running. Please refer to the below example to see how to set those up. If no dictionaries are passed, the program will assume no combinations or keywords are set up.

## Example:

```python
from keyboard_listener import KeyboardListener, Combo, KeyWord

def function_1(string):
  print(f'This function prints {string}')
  
def function_2(string):
  print(f'This function prints {string}')
 

combinations = {

      'function 1': Combo(['alt'], 'f', function_1, 'hello world'), 
        #Function 1 is executed when the user presses Alt+F
      'function 2': Combo(['ctrl','alt'], 'g', function_2, 'goodbye world'), 
        #Function 2 is executed when the user presses Alt+G
      'function 3': Combo(['shift','alt'], 'H', function_2, 'hello again world'), 
        #Be mindful when setting up Combos that include 'shift'. If the Combo includes the shift key, the character must be uppercase.
}

keywords = {

    'keyword_1': KeyWord('keyword1', function_1, 'hello world'),
      #Function 1 is executed when the user types 'keyword1'
    'keyword_2': KeyWord('keyword2', function_2, 'goodbye world') 
      #Function 2 is executed when the user types 'keyword2'
}

keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
```

To see it in action, please take a look at the video titled **keyboard_listener_full_demo.mp4**
