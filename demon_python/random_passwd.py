import random
import pyglet

ventana = pyglet.window.Window(width=800, height=600, resizable=True)

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()=+-*/@#$%&!?'

longitud = 8

passwd = ''

for i in range(longitud):
    passwd += random.choice(caracteres)

print(passwd)

@ventana.event
def on_draw():
    ventana.clear()
    pyglet.app.run()