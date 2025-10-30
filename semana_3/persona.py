class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print('Este es un constructor')

    def saludar(self):
        print(f"Saludo de {self.nombre}")