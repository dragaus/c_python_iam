from persona import Persona
from administrador import Admin
from empledo import Empleado

# class Animal:
#     def hacer_ruido(self):
#         print('ruido generico')

# class Mamifero(Animal):
#     def hacer_ruido(self):
#         super().hacer_ruido()
#         print('Ruido Mamifero')

# vaca = Mamifero()
# toro = Animal()

# vaca.hacer_ruido()


pedro = Admin("Pedro", 45, 30000)
ana = Empleado("Ana", 35, 15000, "Contadora")
maria = Empleado("Maria", 27, 25000, "Programadora")

pedro.saludar()
ana.saludar()
