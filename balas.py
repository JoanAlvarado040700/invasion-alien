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

    def update(self):
        #Actualiza la posicion decimal de la bala 
        self.y -= self.factor_velocidad
        
        #Actualiza la posicion del rect 
        self.rect.y = self.y

    def draw_bala(self):
        #Dibuja la bala en la pantalla
        pygame.draw.rect(self.pantalla, self.color, self.rect)

