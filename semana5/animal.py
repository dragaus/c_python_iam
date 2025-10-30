class Animal:
    def __init__(self, nombre, sonido, crias):
        self.nombre = nombre
        self.sonido = sonido
        self.crias = crias
    
    def hacer_ruido(self):
        print(self.sonido)
        return self.sonido