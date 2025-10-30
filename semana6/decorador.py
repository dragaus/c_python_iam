def decorador_argumentos(a, b):
    def decorador(func):
        def wrapper():
            nombre = "Pepe"
            print(a)
            func()
            print(b)
        return wrapper
    return decorador


@decorador_argumentos("PEDRO", "b")
def hola_mundo():
    print("ESTE ES HOLA MUNDO")

hola_mundo()