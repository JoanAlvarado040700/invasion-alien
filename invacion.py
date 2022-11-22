import pygame as gamer
from config import Configuraciones
from nave import Nave
import eventos as event
from pygame.sprite import Group 



def run_game():
    #Iniciar el juego y crear un obj pantalla
    try:
        gamer.init()
        conf = Configuraciones()
        pantalla = gamer.display.set_mode((
        conf.screen_widh, conf.screen_height))
        gamer.display.set_caption("Invacion aliens")
        #Crear una nave
        nave = Nave(conf, pantalla)

        #Crea un grupo paera almacenar las balar
        balas = Group()

    #Inicia el bucle del juego
        while True:
        #Escucha los eventos de teclado o raaton
            event.verificar_evento(conf, pantalla,nave, balas)
            nave.update()
            balas.update()
        #Actualizar pantalla
            event.actualizar_pantalla(conf, pantalla, nave, balas)
    except gamer.error as e:
        print("Se ha encontrado un error:  ",e)




run_game()