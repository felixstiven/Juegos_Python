from typing import Any
import pygame
import constantes
import math

class Weapons():
    def __init__(self, image, imagen_balas):
        self.imagen_bala = imagen_balas
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.shape = self.imagen.get_rect()
        self.disparada = False
        self.ultimo_disparo = pygame.time.get_ticks()
        
    def update(self, personaje):
        disparo_cooldown = constantes.COOLDOWN_BALAS
        bala = None
        self.shape.center = personaje.shape.center
        if personaje.flip == False:
            self.shape.x = self.shape.x + personaje.shape.width / 1.5
            self.rotar_arma(False)
            
        if personaje.flip == True:
            self.shape.x = self.shape.x - personaje.shape.width / 1.5
            self.rotar_arma(True)
            
        # mover la pistola con el mause 
        mouse_pos = pygame.mouse.get_pos()#metodo seguir mouse  
        distancia_x = mouse_pos[0] - self.shape.centerx 
        distancia_y =-(mouse_pos[1] - self.shape.centery) 
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))
        #print(self.angulo)
        
        # Dectectar los clikc del maus
        if pygame.mouse.get_pressed()[0] and self.disparada == False and pygame.time.get_ticks() - self.ultimo_disparo >=  disparo_cooldown:

            bala = Bullet(self.imagen_bala, self.shape.centerx, self.shape.centery, self.angulo)
            self.disparada = True
            self.ultimo_disparo = pygame.time.get_ticks()
        # Resetear el click del maus
        if pygame.mouse.get_pressed()[0] == False:
            self.disparada = False    
            
        return bala
        # self.shape.y = self.shape.y + 3 # ocasion mejor por porcentajes
        
    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
            
        else:
            
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False) 
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)   
                
        
    def drawn(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.shape)
        # pygame.draw.rect(interfaz, constantes.COLOR_ARMA, self.shape, 1) 
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        
        pygame.sprite.Sprite.__init__(self) 
        self.imagen_bala= image
        self.angulo = angle
        angle = self.angulo
        self.image = pygame.transform.rotate(self.imagen_bala, self.angulo)
        self.rect  = self.image.get_rect()
        self.rect.center = [x, y]
        self.delta_x = math.cos(math.radians(self.angulo)) * constantes.VELOCIDAD_BALAS
        self.delta_y = -math.sin(math.radians(self.angulo)) * constantes.VELOCIDAD_BALAS
    
    def update(self):
        self.rect.x += self.delta_x
        self.rect.y = self.rect.y + self.delta_y    
        # ver si las balas salieron de pantalla
        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VENTANA:
            self.kill()
    
    def drawn (self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery - int(self.image.get_height()))) 
        
        
        