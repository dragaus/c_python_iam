import random

class Pregunta:
    def __init__(self, pregunta: str, 
                respuesta: str, opciones: list[str]):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.opciones = opciones

    def obtener_opciones(self):
        opciones = self.opciones.copy()
        opciones.append(self.respuesta)
        random.shuffle(opciones)
        return opciones

    def es_correcto(self, respuesta: str):
        return respuesta == self.respuesta