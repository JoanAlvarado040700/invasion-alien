import pygame
from pygame.sprite import Sprite 

class Balas(Sprite):
    #Manejar las balas que dispare la nave
    def __init__(self, conf, pantalla, nave):
        super(Balas, self).__init__
        self.pantalla = pantalla


        #Crear una bala rect en (0,0) y luego establece una posicion
        self.rect = pygame.Rect(0,0, conf.bala_width, conf.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        #almacena la posiscion de la bala decimal
        self.y = float(self.rect.y)

        self.color = conf.bala_color
        self.factor_velocidad = conf.bala_factor_velocidad

        #
