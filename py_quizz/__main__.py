from conexion import obtener_pregunta, obtener_preguntas_aleatorias
from classes.quizz import Quizz
print("Juego Py Quizz")

preguntas = obtener_preguntas_aleatorias(4)
quizz = Quizz(preguntas)

pregunta = quizz.siguiente_pregunta()
while pregunta != None:
    print(pregunta.pregunta)
    opciones = pregunta.obtener_opciones()
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}) {opcion}")
    respuesta = int(input("Selecciona la opcion correcta:\n")) - 1

    seleccion = opciones[respuesta]
    print(f"Seleccionaste: {seleccion}")
    
    pregunta, correcto = quizz.responder(seleccion)
    
    if correcto:
        print("¡Buen trabjo seleccionaste la respuesta correcta!")
    else:
        print("Lastima no seleccionesta la respuesta correcta :'(")

print(f"Obtuviste {quizz.puntaje}/{len(quizz.preguntas)}")
# pregunta = obtener_pregunta(1)

# print(pregunta.pregunta)
# opciones = pregunta.obtener_opciones()
# for i, opcion in enumerate(opciones):
#     print(f"{i + 1}) {opcion}")
# respuesta = int(input("Selecciona la opcion correcta:\n")) - 1

# seleccion = opciones[respuesta]
# print(f"Seleccionaste: {seleccion}")
# print(f"Tu respuesta es: {pregunta.es_correcto(seleccion)}")