import pygame
import random

from serpiente import Serpiente
from fruta import Fruta

#Define variables de todo el juego
size_cuadro = 20
cuadros_ancho = 40
cuadros_alto = 30


#Define la serpiente
color_serpiente = pygame.Color(0,255,0)
serpiente = Serpiente(color_serpiente, size_cuadro)

## (x, y)
def obtener_nuevo_lugar_disponible_fruta():
    pos = [
        random.randrange(0, cuadros_ancho -1),
        random.randrange(0, cuadros_alto -1)
    ]

    #[0,5]
    #[[0,0][0,1],[0,2]]
    while pos in serpiente.cuerpo:
        pos = [
            random.randrange(0, cuadros_ancho -1),
            random.randrange(0, cuadros_alto -1)
        ]
    
    return pos


## inicializar pygame
pygame.init()
pygame.display.set_caption("¡Juego serpiente!")


ancho = cuadros_ancho * size_cuadro
alto = cuadros_alto * size_cuadro

size_ventana = (ancho, alto)
ventana = pygame.display.set_mode(size_ventana)

reloj = pygame.time.Clock()
fps = 6

ejecutando = True


color_fruta = pygame.Color(255,0,0)
fruta = Fruta(cuadros_ancho / 2, cuadros_alto / 2, color_fruta, size_cuadro)

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill(pygame.Color(0,0,0))


    # Determinar si la serpiente cambia de direccion
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        serpiente.cambiar_direccion("ARRIBA")
    elif tecla[pygame.K_DOWN]:
        serpiente.cambiar_direccion("ABAJO")
    elif tecla[pygame.K_LEFT]:
        serpiente.cambiar_direccion("IZQUIERDA")
    elif tecla[pygame.K_RIGHT]:
        serpiente.cambiar_direccion("DERECHA")

    # Mover a la serpiente
    serpiente.moverse()

    # Determinar si la fruta se debe de cambiar de poscicion
    if fruta.esta_sobre_la_fruta(serpiente.posicion):
        serpiente.comer()
        fruta.posicion = obtener_nuevo_lugar_disponible_fruta()
    
    # Dibujar la poscicion actual de la serpiente y de la fruta
    fruta.dibujar_fruta(ventana)
    serpiente.dibujar_serpiente(ventana)

    if serpiente.esta_encimada() or serpiente.sale_del_juego(cuadros_ancho, cuadros_alto):
        ejecutando = False


    pygame.display.update()
    reloj.tick(fps)

pygame.quit()