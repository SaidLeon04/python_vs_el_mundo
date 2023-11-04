# importa librerias que se usaran en el codigo
import pygame
import sys
import subprocess

pygame.init() # inicia un proceso de pygame


WIDTH, HEIGHT = 800, 600 # variables para el tamaño de la pantalla
ventana = pygame.display.set_mode((WIDTH, HEIGHT)) # variable con una ventana de pygame
pygame.display.set_caption("Colgado") # coloca un titulo a la pantalla

 
fondo = (252, 252, 116) # color para el fondo de la pantalla 
negro = (0, 0, 0) # color para el texto

 
font = pygame.font.Font(None, 36) # fuente de pygame con tamaño de 36
icon = pygame.image.load('static/icons/icono.png') # icono para el juego

# funcion estandar para crear botones
def create_button(text, x, y, width, height, action=None):
    pygame.draw.rect(ventana, negro, (x, y, width, height)) # dibuja un rectangulo
    text_surface = font.render(text, True, fondo) # parametros para eel texto del boton
    text_rect = text_surface.get_rect() # escribe el texto en el rectangulo
    text_rect.center = (x + width // 2, y + height // 2) # centra el texto
    ventana.blit(text_surface, text_rect) # coloca el texto
    return pygame.Rect(x, y, width, height) # devuelve los parametros del rectangulo


def menu(): # funcion del menu principal
    while True: # bucle infinito hasta recibir falso
        pygame.display.set_icon(icon) # indica el icono que debe recibir la ventana
        for event in pygame.event.get(): # ciclo for para obtener los eventos generales de la ventana
            if event.type == pygame.QUIT: # si el evento cierra la ventana
                pygame.quit() # finaliza pygame
                sys.exit() # termina el proceso
        
        ventana.fill(fondo) # colorea la ventana con el fondo 
        # crea botones usando la funcion y los parametros especificados 
        start_button = create_button("Iniciar Juego", 250, 200, 300, 50) 
        load_button = create_button("Colecciones", 250, 300, 300, 50)
        quit_button = create_button("Salir", 250, 400, 300, 50)

        pygame.display.update() # actuualiza la ventana

        click = pygame.mouse.get_pos() # variable para obtener la posicion del puntero
        if pygame.mouse.get_pressed()[0]: # cuando se presione en estas posiciones
            if start_button.collidepoint(click): # si hubo click en start_button
                subprocess.Popen(["/usr/bin/python3", "juego.py"]) # inicia juego.py
                return False # retorna falso para cerrar el menu
            elif load_button.collidepoint(click): # si hubo click en load_button
                subprocess.Popen(["/usr/bin/python3", "colecciones.py"]) # inicia colecciones.py
                return False # retorna falso para cerrar el menu
            elif quit_button.collidepoint(click): # si hubo click en quit_button
                pygame.quit() # termina la ejecucion de pygame
                return False # retorna falso para cerrar el menu

menu() # llama a la funcion menu
