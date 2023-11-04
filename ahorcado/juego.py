# importa librerias que se usaran en el codigo
import pygame
import random
import numpy as np

# funcion estandar para crear botones
def create_button(text, x, y, width, height):
    pygame.draw.rect(ventana, negro, (x, y, width, height)) # dibuja un rectangulo
    text_surface = escribir.render(text, True, fondo) # parametros para eel texto del boton
    text_rect = text_surface.get_rect() # escribe el texto en el rectangulo
    text_rect.center = (x + width // 2, y + height // 2) # centra el texto
    ventana.blit(text_surface, text_rect)  # coloca el texto
    return pygame.Rect(x, y, width, height) # devuelve los parametros del rectangulo

# funcion para excribir text en una parte de la pantalla
def mostrar_texto(texto):
    text_surface = escribir.render(texto, True, negro) # utiiza la fuente de pygame para escribir
    text_rect = text_surface.get_rect() # alinea el texto 
    text_rect.topleft = (150, 10) # obtiene la posicion arribe e izquierda del texto
    ventana.blit(text_surface, text_rect) # coloca el texto


pygame.init()
ventana = pygame.display.set_mode((800, 600)) # abre una ventana de 800 x 600 px
pygame.display.set_caption("Colgado") # titulo de la ventana
icon = pygame.image.load('static/icons/icono.png') # icono para el juego
fondo = (252, 252, 116) # color para el fondo de la pantalla 
negro = (0, 0, 0) # color para el texto

imagenes = [] # arreglo de imagenes para almacenar las imagenes de cada error
for i in range(7): # for para tomar las 7 imagenes almacenadas
    image = pygame.image.load("static/images/ahorcado" + str(i) + ".png") # caraga la imagen con el numero i 
    imagenes.append(image) # agrega las imagenes al arreglo 


coleccion = [] # arreglo para cargar las palabras jugables por categoria
coleccion = np.loadtxt("db/coleccion.csv", delimiter=",", dtype=str) # convierte el csv a un arreglo de numpy
clave = coleccion[0] # clave para obtener la categoria del juego actual
if clave == "perro": # si la palabra clave es perro 
    categoria = "animales" # la categoria sera animales
elif clave == "python": # si la palabra clave es python
    categoria = "lenguajes de programación" # la categoria sera lenguajes de programacion
elif clave == "manzana": # si la palabra clave es manzana
    categoria = "frutas" # la categoria sera frutas

palabra = random.choice(coleccion) # elige una palabra aleatoria del arreglo con las palabras
palabras_adivinadas = set() # arreglo de tipo set para guardar las palabras ya escritas
errores = 0 # variable para contar los errores y limitarlos

escribir = pygame.font.Font(None, 36) # fuente de pygame

while True: # ciclo infinito para iniciar el juego 
    pygame.display.set_icon(icon) # indica el icono que debe recibir la ventana
    for event in pygame.event.get(): # ciclo for para obtener los eventos generales de la ventana
        if event.type == pygame.QUIT: # si el evento cierra la ventana
            pygame.quit() # finaliza pygame

        if event.type == pygame.KEYDOWN: # detecta si una tecla es presionada
            if event.key >= 97 and event.key <= 122: # limita las teclas detectables a solo minsuculas
                letter = chr(event.key) # convierte el numero de teclas ASCII presionada a caracter
                if letter not in palabras_adivinadas: # si la letras no esta en las ya usadas
                    palabras_adivinadas.add(letter) # se agrega la leta al arreglo 
                    if letter not in palabra: # si la letra no esta en la palabra secreta 
                        errores += 1 # errores incrementa mas 1

    ventana.fill(fondo) # coloca el color del fondo a la ventana
    mostrar_texto(f"Categoria:{categoria}") # # muestra la categoria del palabras actual usando la funcion para escribir texto arriba
  
    display_palabra = "" # la palabra secreta no se muestra 
    for letter in palabra: # recorre la tecla presionada en la palabra secreta 
        if letter in palabras_adivinadas: # si la letra esta en el arreglo de las ya usadas
            display_palabra += letter # se agrega la letra a la palabra seceta
        else: # caso contrario 
            display_palabra += "_ " # la palabra secreta se seguira mostrando con _ 
    text = escribir.render(display_palabra, True, negro) 
    ventana.blit(text, (800 // 2 - text.get_width() // 2, 300))

    if set(palabra) <= palabras_adivinadas:
        text = escribir.render("Ganaste :)", True, negro)
        ventana.blit(text, (800 // 2 - text.get_width() // 2, 200))
    elif errores >= 6:
        text = escribir.render("Perdiste ):, La palabra era: " + palabra, True, negro)
        ventana.blit(text, (800 // 2 - text.get_width() // 2, 200))
    else:
        ventana.blit(imagenes[errores], (800 // 2 - imagenes[errores].get_width() // 2, 50))
    
    reset_button = create_button("salir", 250, 500, 300, 50)
    
    click = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if reset_button.collidepoint(click):
            pygame.quit()
    
    pygame.display.update()
