import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana= pygame.display.set_mode((700,500))
pygame.display.set_caption("Cargar imagen y posición al azar ")
colorfondo= (1,150,70)
colorRectangulo=(255,60,40)
#Cargar una imagen
imagen= pygame.image.load('imagenpython/python.png')
#posicion de la imagen
posX1,posY1= (10,40)
while True:
    ventana.fill(colorfondo)
    #ventana.blit(imagen, (posX1,posY1))
    for i in range(20):
        posX2,posY2=randint(1,500), randint(1,300)
        r, g, b =  randint(0,255) , randint(0,255) , randint(0,255)
        colorRectangulo=(r,g,b)
        pygame.draw.rect(ventana, colorRectangulo,(posX2,posY2,50,50))
    for evento in pygame.event.get():
        if evento.type== QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
