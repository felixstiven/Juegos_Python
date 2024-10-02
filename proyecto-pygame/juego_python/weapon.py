import pygame
import constantes
import math

class Weapons():
    def __init__(self, image):
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.shape = self.imagen.get_rect()
        
    def update(self, personaje):
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
        print(self.angulo)
            
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
        
    
        
        