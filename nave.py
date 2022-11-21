import pygame 

class Nave():
    def __init__(self, pantalla):
        #iniciar la nave y erstablecer 
        try:
            self.pantalla = pantalla
            
            #cargar la imagen de la nave y obtiene su rect
            self.imagen = pygame.image.load("img/nave_1.bmp")
            self.rect = self.imagen.get_rect()
            self.pantalla_rect = pantalla.get_rect()

            #Empieza cada nueva nave en la parte inferior central de la pantalla
            self.rect.centerx = self.pantalla_rect.centerx
            self.rect.bottom = self.pantalla_rect.bottom
        except pygame.error as e:
            print("Error: ",e)

    def blitme(self):
        #Dibujar la nave en una ubicvacion actual
        self.pantalla.blit(self.imagen, self.rect)
