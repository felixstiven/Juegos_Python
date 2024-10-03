import pygame 
import constantes
from personaje import Personaje
from weapon import Weapons

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego") #nombre del juego 

def scalar_igm(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen =  pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

# Importar imagenes 
# Personaje
animaciones = []
for i in range(7):
    img = pygame.image.load(f"proyecto-pygame//juego_python//assets//imagenes//character//player//player_{i}.png")
    img = scalar_igm(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)
    
# Arma     
imagen_pistola = pygame.image.load(f"proyecto-pygame//juego_python//assets//imagenes//character//player//weapons//pistolagame.png")  
imagen_pistola =  scalar_igm(imagen_pistola, constantes.SCALA_ARMA)

#Balas 
imagen_balas = pygame.image.load(f"proyecto-pygame//juego_python//assets//imagenes//character//player//weapons//laser1.png")  
imagen_balas =  scalar_igm(imagen_balas, constantes.SCALA_BALA)

#Crear un jugador de la clase personaje 
jugador = Personaje( 50, 50, animaciones)

#Crear un arma de la clase weporn 
pistola = Weapons(imagen_pistola, imagen_balas)

# crear un grupo de sprite
grupo_balas = pygame.sprite.Group()


#Definir variables de movimiento del jugador 
mover_arriba = False
mover_abajo = False
mover_izquierda  = False
mover_derecha  = False
#Controlar el frame rate
reloj = pygame.time.Clock()


run = True

while run == True:
    # Que valla a 60 fps 
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.COLOR_BG)
    
    #Calcular movimiento del jugador 
    delta_x = 0 
    delta_y = 0 
    
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
        
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
        
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
        
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
        
    #Mover al jugador 
    jugador.movimiento(delta_x, delta_y)   
    #Actualiza estado del jugador
    jugador.update() 
    
    #Actualiza el estado del arma 
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()
    print(grupo_balas)    
    
    # print(f"{delta_x}, {delta_y}") #Pruebas de controles y coordenadas  
                
    # Dibujar al jugador  en la pantalla
    jugador.drawn(ventana)
    # Dibujar el arma en la pantalla 
    pistola.drawn(ventana)
    
    # dibujar balas
    for bala in grupo_balas:
        bala.drawn(ventana)
    
    
    # Para cerrar el juego 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Dectectar eventos en teclas    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True  
                
        # Evento cuando suelte tecla
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
                    
                
            ## print (f"{delta_x}, {delta_y}")    ## pruebas de tecla coordenadas    
            
                
            
    pygame.display.update()        
            
pygame.quit()            