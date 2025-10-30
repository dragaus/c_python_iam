import pygame

class Fruta:
    def __init__(self, x, y, color=pygame.Color(255,0,0), size=20):
        self.posicion = [x,y]
        self.color = color
        self.size = size

    def dibujar_fruta(self, ventana):
        cuadro = pygame.Rect(self.posicion[0] * self.size, self.posicion[1] * self.size, 
                                self.size, self.size)
        pygame.draw.rect(ventana, self.color, cuadro)
    
    def esta_sobre_la_fruta(self, pos):
        return self.posicion == pos