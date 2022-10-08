
import pygame
import sys
from pygame.locals import *

pygame.init()
ventana= pygame.display.set_mode((600,600))
pygame.display.set_caption("Titulo de la ventana")
colorfondo= (1,150,70)
colorLine=(255,128,0)
colorCirculo=(255,255,0)
colorFiguras=(205,0,155)
while True:
    ventana.fill(colorfondo)
    #Lineas
    pygame.draw.line(ventana, colorLine,(60,90), (200,100),40)
    pygame.draw.line(ventana, colorLine,(80,150), (100,150),20)
    pygame.draw.line(ventana, colorLine,(60,30), (250,190),10)
    #Circulos
    pygame.draw.circle(ventana,colorCirculo,(400,110),100,30)
    pygame.draw.circle(ventana,colorCirculo,(500,250),40,20)
    #Figuras
    pygame.draw.rect(ventana,colorFiguras,(100,200,120,250))
    pygame.draw.polygon(ventana,colorFiguras,((300,350),
                        (400,300),(450,400),(390,400)))
    for evento in pygame.event.get():
        if evento.type== QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()