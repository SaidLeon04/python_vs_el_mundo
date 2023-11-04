import pyglet 
from pyglet.gl import *

title = "Calaverita Literaria"
window = pyglet.window.Window(1000, 780, title)
background_image = pyglet.image.load('background.jpg')
background_sprite = pyglet.sprite.Sprite(background_image)


label = pyglet.text.Label("""Una calaca aprendía a programar,
                          
sus errores solución no tenian,

decidio la computadora tirar

y renunciar a la ingeneria.""",
                          font_name='Times New Roman',
                          font_size=20,
                          width=250,
                          x=300, y=400,
                          anchor_x='center', anchor_y='center',
                          multiline=True 
                          )

@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    label.draw()

pyglet.app.run()
