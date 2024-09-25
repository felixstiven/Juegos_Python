import pygame

pygame.init()
screen = pygame.display.set_mode((450,450))
screen2 = pygame.display.set_mode((450,450))
pygame.display.set_caption("Tic-Tac-Tpu")


fondo = pygame.image.load("Static/tictactoe_background.png")
circle = pygame.image.load("Static/circle.png")
esquis = pygame.image.load("Static/x.png")
circle_victory = pygame.image.load("Static/circleganado.png")


fondo = pygame.transform.scale(fondo, (450,450))
circle= pygame.transform.scale(circle, (125,125))
esquis= pygame.transform.scale(esquis, (125,125))
circle_victory = pygame.transform.scale(circle_victory,(200,100))



coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)], #determinar las coordenadas del juego con el ancho y alto de los elementos ver image1
        [(40,300),(165,300),(290,300)]] # esto es algo bidimensional por los dos cohortes y se realiza una tuplas dentro

tablero = [ ["", "", ""],
            ["", "", ""],
            ["", "", ""] ] #bidimensional para guardar las jugadas del jugador 

turno = "X" # en este caso la x siempre va iniciar el juego 
game_over = False #controlar si el juego sigue funcionando o se ha detenido
clock = pygame.time.Clock() #clock estaclecer los freis por segundos del juego

#funcion de iteracion en nuestro tablero 
def graficar_board():
    screen.blit(fondo, (0,0))  
    # iterando el tablero en filas y columnas (for anidado)
    for fila in range(3):  
        for col in range(3):
            #logica de graficar board
            if tablero [fila][col] == "X": # buscanto si contiene algun elemento para gaficar
                dibujar_x(fila,col)
            elif tablero [fila][col] == "O":
                dibujar_o(fila, col)
            
# funciones para dibujar una "x" y "o"
def dibujar_x(fila, col):
    screen.blit(esquis, coor[fila][col])  # imprimir en pantalla (graficar los elementos)
def dibujar_o(fila,col):
    screen.blit(circle, coor[fila][col])   # imprimir en pantalla (graficar los elementos)     
#funcion verificar ganadaor
def verificar_ganador():
    for i in range(3):  
        if tablero[i][0] == tablero[i][1] == tablero [i][2] != "": # buscando que entodas las filas sen iguales y difente a vacio
            return True 
        if tablero [0][i] == tablero[1][i] == tablero[2][i] != "": # buscando que entodas las columnas sen iguales y difente a vacio
            return True
    if tablero [0][0] == tablero [1][1] == tablero[2][2] !="":
        return True
    if tablero [0][2] == tablero [1][1] == tablero[2][0] != "":
        return True  
    
            
    
        
while not game_over: #gameblog por cada iteraacion las va averificar y las va a graficar. 
    clock.tick(30)   # tener una velocidad igual en cualquier equipo
    for event in pygame.event.get(): # va capturas todos los eventos realizados en el jueg0
        if event.type == pygame.QUIT: # click en boton de cerrar (x) finalizara el juego cierra
            game_over = True 
        elif event.type == pygame.MOUSEBUTTONDOWN: # evento click del mouse capturando coordenadas
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425): #restringiendo coordenadas donde se capturara el evento
                fila = (mouseY - 50) // 125 #realizando una resta y division extacta para obtener la posicion indice del evento
                col = (mouseX - 40) // 125
                if tablero[fila][col] == "":
                    tablero[fila][col] = turno
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        print(f"el jugador {turno} ha ganado")
                        game_over = True
                    turno = "O" if turno == "X" else "X" # retorno de turnos si turno es == x retornar o si turno no es == x retorna x                       
    graficar_board()       
    pygame.display.update()         #   actualizar nuestro screen (pantalla)
    
pygame.quit()     # finalizo el ciclo o el usuario cometio un error o dio click al finalizar
    
            
            
            