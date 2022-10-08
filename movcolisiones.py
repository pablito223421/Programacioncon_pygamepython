import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana= pygame.display.set_mode((500,400))
pygame.display.set_caption("Movimiento ratón")
colorfondo= (1,150,70)
colorCuadro1=(255,255,0)
colorCuadro2=(0,255,255)
#Variables
velocidad=15
direccion=True
posX1,posY1 = randint(1, 400), randint(1,300)
posX2,posY2 = randint(1, 400), randint(1,300)
lado=40
while True:
    ventana.fill(colorfondo)
    cuadro1= pygame.draw.rect(ventana,colorCuadro1,(posX1,posY1,lado,lado))
    cuadro2= pygame.draw.rect(ventana,colorCuadro2,(posX2,posY2,lado,lado))
    #detecta colision
    if cuadro1.colliderect(cuadro2):
        print(f"Colisión !!! en coordenada {posX1}: {posY1}")
        posX2,posY2 = randint(1,400), randint(1,300)
        cuadro2.left = posX2 - (lado/2)
        cuadro2.top = posY2 - (lado/2)
    # detecta movimiento raton
    posX1, posY1 = pygame.mouse.get_pos()
    posX1 = posX1 - (lado/2)
    posY1 = posY1 - (lado/2)
    for evento in pygame.event.get():
        if evento.type== QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

