import pynput

def on_move(x, y):
    with open("coordenadas.txt", "a") as doc:
        doc.write("Você moveu o mouse para {0}, {1}\n".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        with open("coordenadas.txt", "a") as doc:
            doc.write("Você clicou o mouse em {0}, {1}\n".format(x, y))

def on_scroll(x, y, dx, dy):
    with open("coordenadas.txt", "a") as doc:
        doc.write("Você scrollou o mouse em ({0}, {1}), ({2}, {3})\n".format(x, y, dx, dy))

with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()