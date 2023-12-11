import pyglet

# Configuración de la ventana
window = pyglet.window.Window(width=600, height=400)
batch = pyglet.graphics.Batch()

# Variables para los bloques y torres
num_blocks = 5
tower_width = 10
tower_height = 200
block_width = 150
block_height = 20
block_spacing = 20

# Lista para almacenar los bloques
blocks = []

# Variable para el bloque seleccionado
selected_block = None
initial_x = 0
initial_y = 0

# Clase Block para representar cada bloque en las torres
class Block:
    def __init__(self, x, y, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.sprite = pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch)
        self.sprite.anchor_x = self.width // 2
        self.sprite.anchor_y = self.height // 2

# Función para dibujar las torres
def draw_towers():
    tower_x_positions = [window.width // 4, window.width // 2, window.width // 4 * 3]
    for x in tower_x_positions:
        pyglet.shapes.Rectangle(x - tower_width // 2, 50, tower_width, tower_height, color=(150, 150, 150)).draw()

# Función para dibujar los bloques en la primera torre
def draw_blocks():
    x = window.width // 4 - block_width // 2 + tower_width // 2
    y = 70
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]
    for i in range(num_blocks):
        block = Block(x, y, block_width - i * 30, block_height, colors[i])
        blocks.append(block)
        y += block.height + block_spacing

# Función para verificar si el mouse está dentro de un bloque
def is_mouse_inside_block(block, x, y):
    return (
        x > block.sprite.x - block.width / 2
        and x < block.sprite.x + block.width / 2
        and y > block.sprite.y - block.height / 2
        and y < block.sprite.y + block.height / 2
    )

@window.event
def on_draw():
    window.clear()
    draw_towers()
    draw_blocks()
    batch.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global selected_block
    if selected_block:
        selected_block.sprite.x = x
        selected_block.sprite.y = y

@window.event
def on_mouse_press(x, y, button, modifiers):
    global selected_block, initial_x, initial_y
    for block in blocks:
        if is_mouse_inside_block(block, x, y):
            selected_block = block
            initial_x = x - block.sprite.x
            initial_y = y - block.sprite.y
            break

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global selected_block
    if selected_block:
        selected_block.sprite.x = x - initial_x
        selected_block.sprite.y = y - initial_y

        # Verificar si el bloque soltado está sobre alguna torre y realizar acciones adicionales si es necesario

pyglet.app.run()
