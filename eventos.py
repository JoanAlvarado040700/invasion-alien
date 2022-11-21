import sys
import pygame

def verificar_evento(nave):
    #Responder a las pulsaciones y a los eventos del Raton
    try:
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    #verifica que el jugador tenga precionada la tecla derecha
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            nave.moving_right = True
                        elif event.key == pygame.K_LEFT:
                            nave.moving_left = True

                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            nave.moving_right = False
                        elif event.key == pygame.K_LEFT:
                            nave.moving_left = False


    except pygame.error as e:
        print("Error: ",e)
        

def actualizar_pantalla(conf, pantalla, nave):
    #Actualizar las imagenes en la pantalla y pasa a la nueva pantallas
        pantalla.fill(conf.bg_color)
        nave.blitme()
    #hacer visible la pantalla dibujada recientemente.
        pygame.display.flip()
