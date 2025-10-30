
class Persona:
    pass

class Profesor(Persona):
    pass

def mi_funcion(nombre):
    if type(nombre) == str:
        print(nombre)
    elif type(nombre) == int:
        print(nombre +1)
    elif type(nombre) == Profesor:
        print("Es profe")
    else:
        print("El tipo no es soportado por esta funcion")
        raise

# juan = Persona()
# hugo = Profesor()
# # mi_funcion(juan)
# mi_funcion(hugo)
# mi_funcion("pepe")
# mi_funcion(1)


def funcion_suma_elementos(*argv):
    suma = 0
    for el in argv:
        suma += el
    return suma

print(funcion_suma_elementos(1,2,800, 300, 600,7000, 600))