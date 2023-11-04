import pygame
import sys
import subprocess
import numpy as np

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Definición de colores
WHITE = (252, 252, 116)
BLACK = (0, 0, 0)

# Fuentes de texto
font = pygame.font.Font(None, 36)
icon = pygame.image.load('static/icons/icono.png')
# Función para crear botones
def create_button(text, x, y, width, height, action=None):
    pygame.draw.rect(win, BLACK, (x, y, width, height))
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    win.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

# Función para mostrar el menú
def menu():
    while True:
        pygame.display.set_icon(icon)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        win.fill(WHITE)

        # Crear botones
        op1_button = create_button("Programación", 250, 100, 300, 50)
        op2_button = create_button("Animales", 250, 200, 300, 50)
        op3_button = create_button("Frutas", 250, 300, 300, 50)
        quit_button = create_button("volver", 250, 400, 300, 50)

        pygame.display.update()

        # Comprobar clic en botones
        click = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if op1_button.collidepoint(click):
                coleccion = ["python","java","javascript","ruby","php","swift","rust","kotlin","go","dart"]
                np.savetxt("db/coleccion.csv", coleccion, delimiter=',', fmt='%s', newline='')
                with open("db/coleccion.csv", 'w') as file:
                    file.write(','.join(coleccion))
                pygame.quit()
                subprocess.Popen(["/usr/bin/python3", "main.py"])
                return False
            elif op2_button.collidepoint(click):
                coleccion = ["perro","gato","elefante","leon","delfin","tiburon",
                             "caballo","oso","canguro","serpiente","mapache"]
                np.savetxt("db/coleccion.csv", coleccion, delimiter=',', fmt='%s', newline='')
                with open("db/coleccion.csv", 'w') as file:
                    file.write(','.join(coleccion))
                pygame.quit()
                subprocess.Popen(["/usr/bin/python3", "main.py"])
                return False
            elif op3_button.collidepoint(click):
                coleccion = ["manzana","platano","naranja","uva","fresa",
                            "kiwi","mango","melon","sandia","cereza","pera"]
                with open("db/coleccion.csv", 'w') as file:
                    file.write(','.join(coleccion))
                pygame.quit()
                subprocess.Popen(["/usr/bin/python3", "main.py"])
                return False
            elif quit_button.collidepoint(click):
                pygame.quit()
                subprocess.Popen(["/usr/bin/python3", "main.py"])
                return False

menu()
