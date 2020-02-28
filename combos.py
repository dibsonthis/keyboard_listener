# Define combo functions here:

def reverse_paste():
    import pyperclip
    data = pyperclip.paste()
    data = data[::-1]
    pyperclip.copy(data)
    print('reverse copy done')

# Insert combos here:

combos = {

'reverse_paste': [ ['ctrl','shift'], 'r', reverse_paste ]

}