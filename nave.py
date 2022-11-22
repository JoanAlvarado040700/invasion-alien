import pygame 

class Nave():
    def __init__(self,conf, pantalla):
        #iniciar la nave y erstablecer 
        try:
            self.pantalla = pantalla
            self.conf = conf
            
            #cargar la imagen de la nave y obtiene su rect
            self.imagen = pygame.image.load("img/nave_1.bmp")
            self.rect = self.imagen.get_rect()
            self.pantalla_rect = pantalla.get_rect()

            #Empieza cada nueva nave en la parte inferior central de la pantalla
            self.rect.centerx = self.pantalla_rect.centerx
            self.rect.bottom = self.pantalla_rect.bottom

            #Almacenar un valor decimal para el centro de la nave
            self.center = float(self.rect.centerx)

            #Bander de moviminetos
            self.moving_right = False
            self.moving_left = False

        except pygame.error as e:
            print("Error: ",e)

    def blitme(self):
        #Dibujar la nave en una ubicvacion actual
        self.pantalla.blit(self.imagen, self.rect)

    def update(self):
        #Actualiza la posicion de la nave segun la Bandera de movimiento
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.conf.velocidad_nave

        if self.moving_left and self.rect.left > 0:
            self.center -= self.conf.velocidad_nave

        #Actualiza el objeto rect
        self.rect.centerx = self.center