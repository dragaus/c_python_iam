import random
from classes.pregunta import Pregunta

class Quizz:
    def __init__(self, preguntas: list[Pregunta]):
        nuevo_order = preguntas.copy()
        random.shuffle(nuevo_order)
        self.preguntas = nuevo_order
        self.contador = 0
        self.puntaje = 0

    def responder(self, respuesta):
        es_correcto = self.preguntas[self.contador-1].es_correcto(respuesta)
        if es_correcto:
            self.puntaje += 1
        nueva_pregunta = self.siguiente_pregunta()
        return (nueva_pregunta, es_correcto)
    
    def siguiente_pregunta(self):
        try :
            pregunta = self.preguntas[self.contador]
        except:
            return None
        self.contador += 1
        return pregunta

    def obtener_preguntas(self):
        return self.preguntas