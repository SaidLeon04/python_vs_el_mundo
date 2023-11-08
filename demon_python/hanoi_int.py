import pyglet
from pyglet import shapes

window = pyglet.window.Window(535, 300)
image = pyglet.resource.image('static/images/humoseta_chiquita.jpg')

label = pyglet.text.HTMLLabel('<b>Presiona el botón</b>', x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

def on_button_click(x, y):
    if label.x - label.content_width/2 < x < label.x + label.content_width/2 and \
       label.y - label.content_height/2 < y < label.y + label.content_height/2:
        print('¡Botón presionado!')
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))
square.opacity = 80
window.on_mouse_press = on_button_click
@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    label.draw()
    square.draw()
pyglet.app.run()