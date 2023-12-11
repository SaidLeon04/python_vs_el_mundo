from pyglet import app
from pyglet.window import Window
from pyglet import image
from pyglet import clock
from pyglet.window import key
import random 
from pyglet import text


window = Window(500,500) # ventana pyglet

@window.event
def on_draw():
    window.clear() # limpia la ventana
    draw_square(snk_x,snk_y,cell_size) # dibuja un cuadrado pequeño que representa la serpiente

    for coords in cola: # dibuja la cola de la serpiente
        draw_square(coords[0],coords[1],cell_size,(0,255,0,0)) # dibuja un cuadrado pequeño por cada punto que se obtenga

    draw_square(fd_x,fd_y,cell_size,(255,0,0,0)) # dibuja la comida

    if game_over: # dibuja la pantalla de game over
        draw_game_over() # funcion game_over


def new_game(): # funcion para iniciar un nuevo juego
    global snk_x,snk_y,snk_dx,snk_dy, game_over, cola # variables globales

    if cell_size < 1 or window.width % cell_size != 0 or window.height % cell_size != 0: # condicion que provoca un error en el funcionamiento
        exit()
    snk_x = window.width // cell_size // 2 * cell_size # posicion inicial de la serpiente en X
    snk_y = window.height // cell_size // 2 * cell_size # posicion inicial de la serpiente en Y
    snk_dx, snk_dy = 0,0 # direccion inicial de la serpiente

    cola = [] # cola de la serpiente
    place_food() # posicion de la comida
    game_over = False # condicion de game over en False
    
def draw_square(x,y,size,colour = (255,255,255,0)): # funcion para dibujar un cuadrado
    img = image.create(size,size,image.SolidColorImagePattern(colour)) # crea una imagen de color
    img.blit(x,y) # dibuja la imagen en la ventana

def place_food(): # funcion para colocar la comida
    global fd_x,fd_y # variables globales
    fd_x = random.randint(0,(window.width // cell_size)-1) * cell_size # posicion aleatoria en X
    fd_y = random.randint(0,(window.height // cell_size)-1) * cell_size # posicion aleatoria en Y


def draw_game_over(): # funcion para dibujar la pantalla de game over
    # label de game over
    game_over_screen = text.Label(f'Puntuación: {len(cola)}',font_size=30,  
                                  x=window.width//2, y=window.height//2,
                                  width=window.width,align='center', 
                                  anchor_x='center', anchor_y='center', 
                                  multiline=True)
    game_over_screen.draw() # dibuja el label

@window.event
def on_key_press(symbol,modifiers): # funcion para mover la serpiente
    global snk_dx,snk_dy, game_over
    if not game_over:
        if symbol == key.LEFT:
            snk_dx -= cell_size
            snk_dy = 0
        elif symbol == key.RIGHT:
            snk_dx += cell_size
            snk_dy = 0
        elif symbol == key.UP:
            snk_dx = 0
            snk_dy += cell_size
        elif symbol == key.DOWN:
            snk_dx = 0
            snk_dy -= cell_size
    else:
        if symbol == key.ENTER: # reinicia el juego
            new_game() # llama a new_game

def update(dt): # funcion para actualizar la ventana
    global snk_x,snk_y, fd_x,fd_y, game_over # variables globales

    if game_over: # condicion para terminar el juego
        return 
    
    if game_over_c(): # condicion para terminar el juego
        game_over = True # game over en True
        return

    cola.append((snk_x,snk_y)) # agrega la posicion de la serpiente a la cola
    snk_x += snk_dx # movimiento de la serpiente en X
    snk_y += snk_dy # movimiento de la serpiente en Y

    if snk_x == fd_x and snk_y == fd_y: # condicion para comer
        place_food() # llama a place_food
    else:
        cola.pop(0) # elimina el primer elemento de la cola

def game_over_c(): # funcion para terminar el juego
    condicion1 = snk_x + snk_dx < 0 or snk_x + snk_dx > window.width - cell_size or snk_y + snk_dy < 0 or snk_y + snk_dy > window.height - cell_size

    condicion2 = (snk_x,snk_y) in cola # condicion para terminar el juego
    return condicion1 or condicion2 # retorna la condicion

cell_size = 20 # tamaño de la serpiente

snk_dx, snk_dy = 0,0 # direccion de la serpiente

snk_x = window.width // cell_size // 2 * cell_size # posicion inicial de la serpiente en X
snk_y = window.height // cell_size // 2 * cell_size # posicion inicial de la serpiente en Y

fd_x,fd_y = 0,0 # posicion de la comida
place_food() # llama a place_food

cola = [] # cola de la serpiente
game_over = False # condicion de game over en False
clock.schedule_interval(update,1/15) # actualiza la ventana cada 1/30 segundos
app.run() # corre la ventana