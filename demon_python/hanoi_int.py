import pyglet # Importa la librería pyglet

window = pyglet.window.Window(width=600, height=400) # Crea una ventana
batch = pyglet.graphics.Batch() # Crea un lote de dibujo

num_blocks = 5 # numero de bloques que se usaran
tower_width = 10 # ancho de las torres
tower_height = 200 # alto de las torres
block_width = 150 # ancho de los bloques
block_height = 20   # alto de los bloques
block_spacing = 20 # espacio entre bloques

blocks = [] # pila para almacenar los bloques

selected_block = None # bloque seleccionado
initial_x = 0 # posicion inicial en x
initial_y = 0 # posicion inicial en y

class Block: # clase para los bloques
    def __init__(self, x, y, width, height, color): # constructor de la clase
        self.width = width # ancho
        self.height = height # alto
        self.color = color # color
        self.sprite = pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch) # crea el bloque
        self.sprite.anchor_x = self.width // 2 # ancla en x
        self.sprite.anchor_y = self.height // 2 # ancla en y

# Función para dibujar las torres
def draw_towers():
    tower_x_positions = [window.width // 4, window.width // 2, window.width // 4 * 3] # posiciones de las torres
    for x in tower_x_positions: # dibuja las torres
        pyglet.shapes.Rectangle(x - tower_width // 2, 50, tower_width, tower_height, color=(255, 255, 255)).draw() # dibuja las torres

# Función para dibujar los bloques en la primera torre 
def draw_blocks():
    x = window.width // 4 - block_width // 12 + tower_width // 4 # posicion inicial en x
    y = 70 # posicion inicial en y
    colors = [(244, 236, 147), (204, 244, 147), (155, 244, 147), (147, 244, 188), (147, 244, 236)] # colores de los bloques
    for i in range(num_blocks): # dibuja los bloques
        block = Block(x, y, block_width - i * 30, block_height, colors[i]) # crea los bloques
        blocks.append(block) # agrega los bloques a la pila
        y += block.height + block_spacing # aumenta la posicion en y

# Función para verificar si el mouse está dentro de un bloque
def is_mouse_inside_block(block, x, y):
    return (
        x > block.sprite.x - block.width / 2 # verifica si el mouse esta dentro del bloque en x
        and x < block.sprite.x + block.width / 2 # verifica si el mouse esta dentro del bloque en x
        and y > block.sprite.y - block.height / 2 # verifica si el mouse esta dentro del bloque en y
        and y < block.sprite.y + block.height / 2 # verifica si el mouse esta dentro del bloque en y
    )

@window.event # evento de dibujar
def on_draw(): # funcion de dibujar
    window.clear()  # limpia la ventana
    draw_towers() # dibuja las torres
    draw_blocks() # dibuja los bloques
    batch.draw() # dibuja el lote
 
@window.event # evento de soltar el mouse
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global selected_block # selecciona el bloque
    if selected_block: # si hay un bloque seleccionado
        selected_block.sprite.x = x # posiciona el bloque en x
        selected_block.sprite.y = y # posiciona el bloque en y

@window.event
def on_mouse_press(x, y, button, modifiers): # evento de presionar el mouse
    global selected_block, initial_x, initial_y # selecciona el bloque, posicion inicial en x, posicion inicial en y
    for block in blocks: # recorre la pila de bloques
        if is_mouse_inside_block(block, x, y): # si el mouse esta dentro del bloque
            selected_block = block # selecciona el bloque
            initial_x = x - block.sprite.x  # posicion inicial en x
            initial_y = y - block.sprite.y # posicion inicial en y
            break # rompe el ciclo

@window.event 
def on_mouse_drag(x, y, dx, dy, buttons, modifiers): # evento de soltar el mouse
    global selected_block # selecciona el bloque
    if selected_block: # si hay un bloque seleccionado
        selected_block.sprite.x = x - initial_x # posiciona el bloque en x
        selected_block.sprite.y = y - initial_y # posiciona el bloque en y

pyglet.app.run() # corre la aplicacion
