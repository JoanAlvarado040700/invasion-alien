import sys 
import pygame as gamer
from config import Configuraciones
from nave import Nave


def run_game():
    #Iniciar el juego y crear un obj pantalla
    try:
        gamer.init()
        conf = Configuraciones()
        pantalla = gamer.display.set_mode((
        conf.screen_widh, conf.screen_height))
        gamer.display.set_caption("Invacion aliens")
        #Crear una nave
        nave = Nave(pantalla)
    except gamer.error as e:
            print("Error: ",e)

    #Inicia el bucle del juego
    try:
        while True:
            #Escucha los eventos de teclado o raaton
            for event in gamer.event.get():
                if event.type == gamer.QUIT:
                    sys.exit()

            #Se le pasa el color al objeto pantalla 
            pantalla.fill(conf.bg_color)
            nave.blitme()
            #hacer visible la pantalla dibujada recientemente.
            gamer.display.flip()
    except gamer.error as e:
        print("error: ",e)




run_game()