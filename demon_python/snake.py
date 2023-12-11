import pyglet
from pyglet.gl import *

ventana = window = pyglet.window.Window(width=600, height=400)

snake_x = 400
snake_y = 300

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
        ('v2i', (10, 15, 30, 35))
    )

if __name__ == "__main__":
    pyglet.app.run()