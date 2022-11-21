import sys
import pygame

def verificar_evento(nave):
    #Responder a las pulsaciones y a los eventos del Raton
    try:
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            nave.rect.centerx +=1

    except pygame.error as e:
        print("Error: ",e)
        

def actualizar_pantalla(conf, pantalla, nave):
    #Actualizar las imagenes en la pantalla y pasa a la nueva pantallas
        pantalla.fill(conf.bg_color)
        nave.blitme()
    #hacer visible la pantalla dibujada recientemente.
        pygame.display.flip()
