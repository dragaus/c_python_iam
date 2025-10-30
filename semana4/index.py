## Juego de ahorcado

## palabra secreta
## [a-z]
## [e]
## _ _ _ _ _ _ 

##   a   o
## _ _ _ _

## _ a _ o

## x cantidad de oportunidades para adivinar

import click
import instrucciones
import re
import random
from ahorcado import estados_ahorcado
from palabras import palabras

palabra_secreta = ""
letras_usadas = []
num_errores = 0

def mostrar_resultados():
    resultado = ""
    for caracter in palabra_secreta:
        if caracter in letras_usadas:
            resultado += caracter + " "
            continue
        resultado += "_ "
    print(estados_ahorcado[num_errores])
    print(resultado)

def obetener_intento():
    global num_errores
    input_valido = False
    intento = ""

    while not input_valido:
        intento = input('¿Que letra crees que tiene la palabra secreta?')
        if len(intento) != 1:
            print("Ingresa solo una letra")
            continue

        if not re.match("[a-zA-ZÑñ]", intento):
            print("Ingresa un caracter valido")
            continue

        if intento in letras_usadas:
            print(f'Ya intentaste con esta letra: {intento}, Prueba de nuevo')
            continue

        input_valido = True

        

    if intento in palabra_secreta:
        print("Advinaste una letra")
    else:
        num_errores += 1
        print("has fallado")
    return intento.lower()

def ha_adivinado_palabra():
    for caracter in palabra_secreta:
        if caracter in letras_usadas:
            continue
        return False
    return True


@click.command
@click.option("--dif", default="f", help="Selecciona facil (f), medio (m), dificil (d)")
def juego(dif):
    global palabra_secreta
    instrucciones.mostrar_instrucciones(2)
    palabra_secreta = palabras[random.randint(0, len(palabras) - 1)]
    print(f"Tu palabra tiene {len(palabra_secreta)} letras")

    adivino_palabra = False
    while not adivino_palabra and num_errores < len(estados_ahorcado): 
        mostrar_resultados()
        letra_adivinada = obetener_intento()
        letras_usadas.append(letra_adivinada)
        adivino_palabra = ha_adivinado_palabra()
    
    if adivino_palabra:
        print("Ganaste")
    else:
        print("Perdiste")

    print(f"la palabra secreta era: {palabra_secreta}")

seguir_juego = True

while seguir_juego:
    juego(standalone_mode=False)
    respuesta = input('¿Quieres jugar de nuevo(S/N)?')
    seguir_juego = respuesta == "s"
    letras_usadas.clear()
    num_errores = 0
