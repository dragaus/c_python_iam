# nombre = input("Cual es su nombre?")

# if nombre == "Pedro":
#     print(f"Buenos dias Dr. {nombre}")
# elif nombre == "Juan":
#     print(f"Buen dia ingeniero {nombre}")
# else:
#     print(f"Buenos dias {nombre}")
#     print("Ejecuccion 1")
   
# print("Ejecuccion 2")

# == > < >= <=
def obtener_nombre():
    return input("¿Cual es tu nombre?")

def ingreso():
    edad = int(input("¿Cual es tu edad?"))
    if edad >= 18:
        print("puedes entrar")
    elif edad > 11:
        ingreso_menores()
    else:
        prohibir_ingreso()

def ingreso_menores():
    respuesta = input('Tienes permiso de tus padres')
    print(respuesta)
    print(respuesta.lower())
    if respuesta.lower() == "si":
        print("puedes entrar")
    else:
        prohibir_ingreso()
        
def prohibir_ingreso():
    print("No puedes entrar")

def saluda(nombre: str):
    print(f"Buenos dias {nombre}")


numero = 0
while numero < 100:
    print(numero)
    numero += 1

while True:
    nombre = obtener_nombre()
    ingreso()



