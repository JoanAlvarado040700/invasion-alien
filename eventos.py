import sys
import pygame
from balas import Balas

def evento_keydown(event,conf, pantalla,nave, balas):
    #Respomde a las pulsaciones de teclas 
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    #Crea una nueva bala y la agrega al grupo balas
    elif event.key == pygame.K_SPACE:
        balas.add(Balas(conf, pantalla, nave))
        

def evento_keyUp(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False    


def verificar_evento(conf, pantalla,nave, balas):
    #Responder a las pulsaciones y a los eventos del Raton
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                    #verifica que el jugador tenga precionada la tecla derecha
            elif event.type == pygame.KEYDOWN:
                    evento_keydown(event,conf, pantalla,nave, balas)
            elif event.type == pygame.KEYUP:
                        evento_keyUp(event, nave)

    except pygame.error as e:
        print("Error: ",e)
        

def actualizar_pantalla(conf, pantalla, nave, balas):
    #Actualizar las imagenes en la pantalla y pasa a la nueva pantallas
    pantalla.fill(conf.bg_color)
    #Redibuja las balas detras de la nave y los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()

    nave.blitme()

    #hacer visible la pantalla dibujada recientemente.
    pygame.display.flip()
