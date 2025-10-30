import pygame

class Serpiente:
    #self posicion se refiere al lugar donde estara la cabeza de la serpiente
    def __init__(self, color=pygame.Color(0,255,0), size=20):
        self.color = color
        self.size = size
        self.longitud = 3
        self.posicion = [2, 0]
        self.cuerpo = [[i, 0] for i in range(self.longitud)][::-1]
        ## [[0,0],[1,0],[2,0]]
        ## [[2,0],[1,0],[0,0]]
        self.direccion = 'DERECHA'
    
    def dibujar_serpiente(self, ventana):
        for pos in self.cuerpo:
            cuadro = pygame.Rect(pos[0] * self.size, pos[1] * self.size,
                                self.size, self.size)
            pygame.draw.rect(ventana, self.color, cuadro)
    
    def moverse(self):
        if self.direccion == 'DERECHA':
            self.posicion[0] += 1
        elif self.direccion == 'IZQUIERDA':
            self.posicion[0] -= 1
        elif self.direccion == "ARRIBA":
            self.posicion[1] -=1
        elif self.direccion == "ABAJO":
            self.posicion[1] +=1
        
        ## cuerpo tenemos que agregar la poscion actual de la serpiente
        ## [[3,0],[2,0],[1,0],[0,0]]
        self.cuerpo.insert(0, list(self.posicion))

        ## Elimar las posciones mas alla de la longitud
        ## [[3,0],[2,0],[1,0]]
        if len(self.cuerpo) > self.longitud:
            self.cuerpo.pop()
    
    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion == "ARRIBA" and self.direccion != "ABAJO":
            self.direccion = nueva_direccion
        if nueva_direccion == "ABAJO" and self.direccion != "ARRIBA":
            self.direccion = nueva_direccion
        if nueva_direccion == "IZQUIERDA" and self.direccion != "DERECHA":
            self.direccion = nueva_direccion
        if nueva_direccion == "DERECHA" and self.direccion != "IZQUIERDA":
            self.direccion = nueva_direccion
    
    def comer(self):
        self.longitud += 1

    def esta_encimada(self):
        ## [[2,0],[1,0],[0,0]]
        ## [[1,0],[0,0]] -> [1:]
        return self.posicion in self.cuerpo[1:]
    
    def sale_del_juego(self, limite_x, limite_y):
        if self.posicion[0] < 0 or self.posicion[0] >= limite_x:
            return True
        if self.posicion[1] < 0 or self.posicion[1] >= limite_y:
            return True
        return False
