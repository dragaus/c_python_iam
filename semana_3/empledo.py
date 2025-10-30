from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, cargo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        self.cargo = cargo