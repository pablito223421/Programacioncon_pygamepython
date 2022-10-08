
import pygame
import sys
from pygame.locals import *

pygame.init()
ventana= pygame.display.set_mode((400,300))
pygame.display.set_caption("Titulo de la ventana")
colorfondo= (1,150,70)
colorLine(255,128,0)

while True:
    ventana.fill(colorfondo)
    pygame.draw.line(ventana, colorLine,(20,30), (120,100),20)
    for evento in pygame.event.get():
        if evento.type== QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()