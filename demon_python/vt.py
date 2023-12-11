import pyglet

# Creamos una ventana
window = pyglet.window.Window(width=400, height=300)

# Lista de coordenadas y tamaños para los rectángulos
rectangles = [
    (50, 50, 100, 50),    # (x, y, width, height)
    (150, 100, 80, 120),
    (250, 200, 70, 90),
    (100, 200, 120, 80),
    (300, 100, 90, 60)
]

@window.event
def on_draw():
    window.clear()
    # Dibujamos cada rectángulo en la lista
    for rect in rectangles:
        x, y, width, height = rect
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
            ('v2i', (x, y, x + width, y, x + width, y + height, x, y + height))
        )

if __name__ == "__main__":
    pyglet.app.run()
